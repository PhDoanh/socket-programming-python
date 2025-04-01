import socket

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

clientName = input('Enter your name: ')
clientSocket.send(clientName.encode())

while True:
    try:
        sentence = input(f'{clientName}: ')
        clientSocket.send(sentence.encode())
        
        if sentence.lower() == 'bye':
            break
        
        response = clientSocket.recv(1024).decode()
        print('Server:', response)
        
        if response.lower() == 'bye':
            break
    except IOError:
        print("Connection may be closed from server!")
        break

clientSocket.close()
