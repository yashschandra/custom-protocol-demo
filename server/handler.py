import _thread
from constants import KEY
import json

class Handler():

    def __init__(self):
        self.buffer_size = 1024

    def handle_connection(self, client_socket, address):
        _thread.start_new_thread(self.handle_client, (client_socket, address, ))

    def handle_client(self, client_socket, address):
        while True:
            data = json.loads(client_socket.recv(self.buffer_size).decode())
            response = self.handle_data(data)
            client_socket.send(json.dumps(response).encode())
            if response['message'] == 'bye':
                client_socket.close()
                break

    def handle_data(self, data):
        response = {
            "key": KEY,
            "type": "response"
        }
        if self.validate(data):
            message = data['message']
            if message == 'hello':
                response_message = 'hello ' + data['protocol']
            else:
                response_message = message
        else:
            response_message = 'invalid request'
        response['message'] = response_message
        return response

    def validate(self, data):
        if data['key'] == KEY:
            return True
        return False