import asyncio
import socket


class Client:       #Class mit dem Namen CLient
    def __init__(self):
        self.client_conn = None     #Setzt alle Variablen auf None oder eine bestimmt Address
        self.address = ("127.0.0.1", 50000)
        self.server = None

    def client_connect(self):
        self.client_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Erzeugt einen Socket
        try:
            self.client_conn.connect(self.address)          #Versucht eine Verbindung mkit dem Host herzustellen
            return True
        except ConnectionRefusedError:
            print("HOST HAS TO BE SELECTED FIRST")          #Wenn Verbindung nicht möglich wird dass hier ausgeführt
            return False                                    #Verhindert Crash des Programms

    def write(self, message: bytes):                        #Write Function um mit dem Server zu Kommunizieren zu können
        self.client_conn.send(message)

    def recv(self):                                         #Read Function um Daten von dem Server zu bekommen
        return self.client_conn.recv(1024)


if __name__ == '__main__':
    client = Client()
    client.client_connect()
