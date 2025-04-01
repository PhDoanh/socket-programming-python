from socket import * 
from threading import *

def handleClient(connectionSocket):
	try:
		message = connectionSocket.recv(1024).decode() # decode msg from bytes to string
		filename = message.split("\r\n")[0].split()[1] # get the first line of response and extract filename         
		
		if filename == '/':
			filename = '/HelloWorld.html'

		with open(".." + filename) as f:               
			outputdata = f.read()

		#Send HTTP header lines into socket 
		connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
		connectionSocket.send("Content-Type: text/html\r\n".encode())
		connectionSocket.send(f"Content-Length: {len(outputdata)}\r\n".encode())
		connectionSocket.send("\r\n".encode())

		#Send the content of the requested file to the client 
		connectionSocket.send(outputdata.encode()) 
	except IOError: 
		#Send response message for file not found 
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
		connectionSocket.send("Content-Type: text/html\r\n".encode())
		connectionSocket.send("\r\n".encode())
		connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())

	connectionSocket.close()

# Prepare a server socket 
serverPort = 80 # default for http
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

while True: 
	# Establish the connection 
	print('Ready to serve...') 
	connectionSocket, addr = serverSocket.accept()  
	clientThread = Thread(target=handleClient, args=(connectionSocket,))
	clientThread.start()
