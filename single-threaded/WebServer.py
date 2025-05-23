#import socket module 
from socket import * 
import sys # In order to terminate the program 

#Prepare a sever socket 
serverPort = 80 # default for http
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

while True: 
	#Establish the connection 
	print('Ready to serve...') 
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024).decode()
		filename = message.split("\r\n")[0].split()[1]        

		if filename == '/':
			filename = '/HelloWorld.html'

		f = open(".." + filename)                         
		outputdata = f.readlines()

		#Send one HTTP header line into socket 
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

		#Send the content of the requested file to the client 
		for i in range(0, len(outputdata)):            
			connectionSocket.send(outputdata[i].encode()) 
		
		connectionSocket.send("\r\n".encode()) 
		connectionSocket.close() 
	except IOError: 
		#Send response message for file not found 
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())

		#Close client socket 
		connectionSocket.close()
	
	serverSocket.close() 
	sys.exit() #Terminate the program after sending the corresponding data