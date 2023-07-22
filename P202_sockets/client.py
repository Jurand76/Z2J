import socket as s
import json


class Client:
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    def __init__(self):
        self.connection = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.connection.connect((self.HOST, self.PORT))

    def communication(self, query):
        data = query.encode('utf8')
        self.connection.sendall(data)
        response = self.connection.recv(1024).decode('utf8')
        return response


client = Client()

query = ""
while query != "stop":
    query = input("Input server query: ")
    print(f"{client.communication(query)}")

