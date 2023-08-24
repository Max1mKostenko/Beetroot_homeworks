import socket

msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)


step = 3
res = ""
for char in msgFromClient:
    if char.isalpha():
        if char.isupper():
            num_of_ascii_table = 65
        else:
            num_of_ascii_table = 97
        new_char = chr((ord(char) - num_of_ascii_table + step) % 26 + num_of_ascii_table)
    else:
        new_char = char
    res += new_char
msg = f"Message from Server {res}"
print(msg)
