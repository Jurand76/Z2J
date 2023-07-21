import socket as s


class Client:
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    def __init__(self):
        self.connection = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.connection.connect((self.HOST, self.PORT))

    def communication(self):
        query = "uptime".encode('utf8')
        self.connection.sendall(query)
        response = self.connection.recv(1024).decode('utf8')
        return response


client = Client()
print(f"Received: {client.communication()}")
