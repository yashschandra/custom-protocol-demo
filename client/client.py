from clientsocket import ClientSocket

class Client():

    def __init__(self):
        self.client_socket = ClientSocket()

    def connect(self, host, port):
        self.client_socket.connect(host, port)

    def send_data(self, data):
        data = self.client_socket.send_data(data)
        return data

    def close(self):
        self.client_socket.close()