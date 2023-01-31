import socket
from chess4b.network import Client


class Server(Client):           #Classe mit dem Namen Server (Client) = Dass alle Variablen des Clients auch bei dem Server vorhanden sind
    def __init__(self):
        super().__init__()
        self.server = None      #Setzt alle Variablen auf nichts sodass es zu keinen Problemen kommt
        self.conn = None
        self.addr = None

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Setzt einen Socket auf
        self.server.bind(self.address)
        self.server.listen(1)                                            #Wartet nur auf eine Connection
        self.conn, self.addr = self.server.accept()                      #Sobald ein Client connected speichert es seinen Port und seine Addresse

    def write(self, message: bytes):                #Write Funktion zum Kommunizieren mit dem Server
        self.conn.send(message)

    def recv(self):                                 #Read Funktion um Messages des Clients zu empfangen
        return self.conn.recv(1024)


if __name__ == '__main__':
    server = Server()
    server.start_server()
    # server.write()
