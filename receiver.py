import socket, station, datetime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.0.127', 1234))
s.listen(5)

stations = []

#ToDo: Thread para mostrar os dispositivos presentes na tela

while True:
	con, client = s.accept()
	print(f"Conectado a {client}")
	msg = con.recv(1024).decode('utf-8')

	print(f"{client}: {msg}")
	print(f"encerrando conexão com {client}")
	con.shutdown(socket.SHUT_RDWR)
	con.close()

	time_string = msg.split('|')[1]
	year = int(time_string.split('-')[0])
	month = int(time_string.split('-')[1])
	day = int(time_string.split('-')[2].split(' ')[0])
	#hour = int(a.split('-')[2].split(' ')[0].split(':')[0])
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
                #print(msg.split('|')[0], msg.split('|')[1])

	print(len(stations))
