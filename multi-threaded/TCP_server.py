import socket
import threading

def handleClient(conn):
    clientName = conn.recv(1024).decode().strip()

    while True:
        response = conn.recv(1024).decode()
        if not response:
            break
        print(f"{clientName}: {response}")
        if response.lower() == 'bye':
            break
        sentence = input(f"Server to {clientName}: ")
        conn.send(sentence.encode())
        if sentence.lower() == 'bye':
            break

    conn.close()
    print(f"Connection with {clientName} closed.\n")

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

print('The server is ready to receive')

while True:
    conn, addr = serverSocket.accept()
    
    clientThread = threading.Thread(target=handleClient, args=(conn,))
    clientThread.start()
