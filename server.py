import socket
import threading

def handle_client(client_socket, address):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break 

        print(f"Received from {address[0]}:{address[1]}: {data}")
        client_socket.send(data.encode('utf-8'))
    client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
