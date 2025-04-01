import socket

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    # print("Connection from", addr)
    clientName = connectionSocket.recv(1024).decode().strip()
    # print(f"{clientName} is connected")

    while True:
        try:
            response = connectionSocket.recv(1024).decode()
            if not response:
                break
            print(f"{clientName}: {response}")
            
            if response.lower() == 'bye':
                break

            sentence = input('Server: ')
            connectionSocket.send(sentence.encode())
            
            if sentence.lower() == 'bye':
                break
        except IOError:
            print("Connection may be closed from client!")
            break

    connectionSocket.close()
    print(f"Connection with {clientName} closed. Waiting for next client...\n")
