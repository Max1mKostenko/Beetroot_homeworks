import socket


def caesar_encrypt(massage, key):
    encrypted_massage = ""
    for char in massage:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a' + shift)) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A' + shift)) % 26 + ord('A'))
            encrypted_massage += encrypted_char
        else:
            encrypted_massage += char
    return encrypted_massage


HOST = "127.0.0.1"
PORT = 20001
bufferSize = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((HOST, PORT))
print("UDP server up and listening")

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    massage = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Massage from Client:{}".format(massage)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    # Get the encryption key from the client
    encryption_key = int(input("Enter encryption key: "))  # You can also send this key from the client

    # Encrypt the massage using Caesar cipher
    encrypted_massage = caesar_encrypt(massage.decode(), encryption_key)
    encrypted_bytes = str.encode(encrypted_massage)

    UDPServerSocket.sendto(encrypted_bytes, address)
