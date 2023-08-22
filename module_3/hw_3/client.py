import socket


def caesar_decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a' - shift)) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A' - shift)) % 26 + ord('A'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message


msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

encryption_key = int(input("Enter encryption key: "))  # You can also generate this key randomly

msgFromServer, serverAddress = UDPClientSocket.recvfrom(bufferSize)
decrypted_message = caesar_decrypt(msgFromServer.decode(), encryption_key)

print("Message from Server (Decrypted):", decrypted_message)
