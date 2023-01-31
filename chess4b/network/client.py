import asyncio
import socket


class Client:       #Classe mit dem Namen Client
    def __init__(self):
        self.client_conn = None
        self.address = ("127.0.0.1", 50000)  #Variable Address die IP des Servers geben
        self.server = None

    def client_connect(self):           #Funktion

        self.client_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Aufsetzen eines Sockets
        try:
            self.client_conn.connect(self.address)      #Versucht sich mit dem Server zu verbinden
            return True
        except ConnectionRefusedError:                  #Wenn die Verbindung nicht möglich ist wird diese Aufgerufen
            return False                                #Verhindert Programmcrash

    def write(self, message: bytes):            #Write Funktion zum Kommunitziern mit den Server
        self.client_conn.send(message)

    def recv(self):                             #Read FUnktion um Messages von dem Server zu empfangen
        return self.client_conn.recv(1024)


if __name__ == '__main__':
    client = Client()
    client.client_connect()
