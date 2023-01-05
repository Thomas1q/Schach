import socket
from network import Client


class Server(Client):
    def __init__(self):
        super().__init__()
        self.server = None

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.address)
        self.server.listen(1)
        while True:
            client_conn, client_addr = self.server.accept()
            print(client_conn.recv(1024).decode())

    def write(self):
        self.client_conn.send("Kann spielfeld übertragen".encode())


if __name__ == '__main__':
    server = Server()
    server.start_server()
    # server.write()
