import sys
from socket import *

def main():
    if len(sys.argv) != 4:
        print("Usage: python client.py <server> <port> <path>")
        sys.exit(1)
    
    server = sys.argv[1]
    port = int(sys.argv[2])
    path = sys.argv[3]
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((server, port))
    
    requestLine = f"GET {path} HTTP/1.1\r\n"
    hostHeader = f"Host: {server}\r\n"
    endHeader = "\r\n"
    request = requestLine + hostHeader + endHeader
    
    clientSocket.send(request.encode())
    
    response = ""
    while True:
        chunk = clientSocket.recv(4096).decode()
        if not chunk:
            break
        response += chunk
    
    print(response)
    
    clientSocket.close()

if __name__ == "__main__":
    main()
