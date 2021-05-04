import socket, station

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.0.127', 1234))
s.listen(5)

stations = []

#ToDo: Thread para mostrar os dispositivos presentes na tela

while True:
	con, client = s.accept()
	print(f"Conectado a {client}")
	msg = con.recv(1024)
	
	print(f"{client}: {msg}")
	print(f"encerrando conexão com {client}")
	con.shutdown(socket.SHUT_RDWR)
	con.close()

    for station in stations:
        if station.get_address() == msg.split('|')[0]:
            station.new_detection(msg.split('|')[1])
            break
    else:
        stations +=  [station.Station(msg.split('|')[0], msg.split('|')[1])]


    stations += [Station()]
    
