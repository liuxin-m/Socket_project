
#!/usr/bin/env python
import socket

HOST_name='localhost'   #Server IP
PORT=8888    #Server port
CONT=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
CONT.connect((HOST_name,PORT))
while True:
	USER_input=raw_input('Please input your command: \n').strip()
	if len(USER_input)==0:
		continue
	CONT.sendall(USER_input)
	print 'command sending , please wait....'
	DATA=CONT.recv(1024)
	print 'recevied server messages: \n',DATA
CONT.close()
