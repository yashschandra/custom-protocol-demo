import socket
from handler import Handler

class ServerSocket():

    def __init__(self, max_connection, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(max_connection)
        self.handler = Handler() 

    def start(self):
        while True:
            (client_socket, address) = self.server_socket.accept()
            self.handler.handle_connection(client_socket, address)