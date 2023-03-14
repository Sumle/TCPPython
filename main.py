from socket import *
import threading

def handle_client(connection_socket, address):
    print(address[0])
    sentence = connection_socket.recv(1024).decode()
    print(sentence)
    capitalized_sentence = sentence.upper()
    lower_sentence = sentence.lower()
    connection_socket.send(capitalized_sentence.encode())
    connection_socket.send(lower_sentence.encode())
    connection_socket.close()


serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    while True:
        sentence = connectionSocket.recv(1024).decode()
        response = "Didn't understand: " + sentence
        sentence = sentence.lower()
        if sentence == "close\r\n":
            print("Closed")
            connectionSocket.send("Closing down".encode())
            connectionSocket.close()
            break
        elif sentence.startswith("upper:"):
            sentence = sentence[6:]
            print(sentence)
            response = sentence.upper()
        elif sentence.startswith("lower:"):
            sentence = sentence[6:]
            print(sentence)
            response = sentence.lower()
        elif sentence.startswith("reverse:"):
            sentence = sentence[8:]
            print(sentence)
            response = sentence[::-1]
        connectionSocket.send(response.encode())
    connectionSocket.close()