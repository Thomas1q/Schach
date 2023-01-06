import socket
from chess4b.network import Client


class Server(Client):
    def __init__(self):
        super().__init__()
        self.server = None
        self.conn = None
        self.addr = None

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.address)
        self.server.listen(1)
        self.conn, self.addr = self.server.accept()

    def write(self, message: bytes):
        self.conn.send(message)

    def recv(self):
        return self.conn.recv(1024)


if __name__ == '__main__':
    server = Server()
    server.start_server()
    # server.write()
