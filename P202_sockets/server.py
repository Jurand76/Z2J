import json
import socket
from datetime import datetime


class Server:
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 65432
        self.start_time = datetime.now()
        self.VERSION = str(
            f"Server at host {self.HOST} working on port {self.PORT}. Software version 1.0. Server started {self.start_time}")

    def get_server_time(self):
        time_now = datetime.now()
        return time_now - self.start_time

    def help_command(self):
        help_data = {"uptime": "zwraca czas zycia serwera",
                     "info": "zwraca numer wersji serwera, date jego utworzenia",
                     "help": "zwraca liste dostepnych komend",
                     "stop": "zatrzymuje jednoczesnie serwer i klienta"}
        return help_data

    def server_answer(self, connection, response):
        connection.sendall(json.dumps(response).encode('utf8'))

    def server_start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024).decode('utf8')
                    print(f"Received data: {data}")
                    if data == "info":
                        response = self.VERSION
                        self.server_answer(conn, response)
                    if data == "uptime":
                        response = str(self.get_server_time())
                        self.server_answer(conn, response)
                    if data == "help":
                        response = self.help_command()
                        self.server_answer(conn, response)
                    if data == "stop":
                        response = "Server stopped by user"
                        self.server_answer(conn, response)
                        break


server = Server()
server.server_start()
