import socket

class ClientSocket():
    
    def __init__(self):
        self.buffer_size = 1024
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.client_socket.connect((host, port))

    def send_data(self, data):
        self.client_socket.send(data.encode())
        response = self.client_socket.recv(self.buffer_size).decode()
        return response

    def close(self):
        self.client_socket.close()