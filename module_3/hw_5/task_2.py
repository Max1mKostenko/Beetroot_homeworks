import socket
import threading


def client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.send(data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()


def main(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"Listening on {host}:{port}")

    try:
        while True:
            conn, addr = server.accept()
            print(f"Accepted connection from {addr}")

            thr = threading.Thread(target=client, args=(conn,))
            thr.start()
    except KeyboardInterrupt:
        print("Server shutting down.")
        server.close()


if __name__ == "__main__":
    main('127.0.0.1', 12345)
