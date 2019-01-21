from serversocket import ServerSocket

MAX_CONNECTION = 5
PORT = 9210
HOST = '0.0.0.0'

if __name__ == '__main__':
    server_socket = ServerSocket(MAX_CONNECTION, HOST, PORT)
    server_socket.start()