import socket

HOST = "127.0.0.1"
PORT = 20001
bufferSize = 1024

msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)


UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((HOST, PORT))
print("UDP server up and listening")


while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    UDPServerSocket.sendto(bytesToSend, address)
