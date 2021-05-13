import socket, station, datetime, time, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.0.127', 1234))
s.listen(5)

stations = []


def update():
	while True:
		for st in stations:
			st.update()
			if st.state.is_present or st.state.is_potential_out:
                            print(st.get_address())

		print('\n')
		print('/-\-'*15)
		#print(stations)
		print('\n')
		print(len(stations))
		print('\n')
		print(str(datetime.datetime.now().time())[:8])
		time.sleep(2)


#ToDo: Thread para mostrar os dispositivos presentes na tela
#ToDo tratamento de exceções
if __name__ == '__main__':
	update_thread = threading.Thread(target=update)
	update_thread.daemon = True
	update_thread.start()


	while True:
		con, client = s.accept()
		#print(f"Conectado a {client}")
		msg = con.recv(1024).decode('utf-8')

		#print(f"{client}: {msg}")
		#print(f"encerrando conexão com {client}")
		con.shutdown(socket.SHUT_RDWR)
		con.close()

		time_string = msg.split('|')[1]
		year = int(time_string.split('-')[0])
		month = int(time_string.split('-')[1])
		day = int(time_string.split('-')[2].split(' ')[0])
		hour = int(time_string.split(' ')[1].split(':')[0])
		minute = int(time_string.split(' ')[1].split(':')[1])
		second = int(time_string.split(' ')[1].split(':')[2].split('.')[0])
		detection_time = datetime.datetime(year, month, day, hour, minute, second)


		for st in stations:
			if st.get_address() == msg.split('|')[0]:
				st.new_detection(detection_time)
				break
		else:
			stations +=  [station.Station(msg.split('|')[0], detection_time)]


