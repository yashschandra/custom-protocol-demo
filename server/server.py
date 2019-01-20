from serversocket import ServerSocket

MAX_CONNECTION = 5
PORT = 9210

if __name__ == '__main__':
    server_socket = ServerSocket(MAX_CONNECTION, PORT)
    server_socket.start()