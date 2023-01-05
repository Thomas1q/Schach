import asyncio
import socket


class Client:
    def __init__(self):
        self.client_conn = None
        self.address = ("127.0.0.1", 50000)
        self.server =None


    def client_connect(self):
        self.client_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_conn.connect(self.address)



    def write(self):
        self.client_conn.send("Hello".encode())

if __name__ == '__main__':
    client=Client()
    client.client_connect()
    client.write()