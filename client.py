import socket
import threading

def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break 
        print(f"Received from server: {data}")

def start_client():
    host = '127.0.0.1'
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Enter message (or 'exit' to quit): ")
        client_socket.send(message.encode('utf-8'))

        if message.lower() == 'exit':
            break
    client_socket.close()

if __name__ == "__main__":
    start_client()
