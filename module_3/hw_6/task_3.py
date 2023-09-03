import socket
import multiprocessing


def client(client_socket):
    print(f"Connected: {multiprocessing.current_process().name}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.send(data)

    client_socket.close()
    print(f"Disconnected: {multiprocessing.current_process().name}")


def main(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")

            client_process = multiprocessing.Process(target=client, args=(conn,))
            client_process.start()
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main('127.0.0.1', 12345)
