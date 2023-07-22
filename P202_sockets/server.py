import json
import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 65432
start_time = datetime.now()
VERSION = str(f"Server at host {HOST} working on port {PORT}. Software version 1.0. Server started {start_time}")
print(start_time)


def get_server_time():
    global start_time
    time_now = datetime.now()
    return time_now - start_time


def help_command():
    help_data = {"uptime": "zwraca czas zycia serwera",
                 "info": "zwraca numer wersji serwera, date jego utworzenia",
                 "help": "zwraca liste dostepnych komend",
                 "stop": "zatrzymuje jednoczesnie serwer i klienta"}
    return help_data


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode('utf8')
            print(f"Received data: {data}")
            if data == "info":
                response = VERSION
                conn.sendall(json.dumps(response).encode('utf8'))
            if data == "uptime":
                response = str(get_server_time())
                conn.sendall(json.dumps(response).encode('utf8'))
            if data == "help":
                response = help_command()
                conn.sendall(json.dumps(response).encode('utf8'))
            if data == "stop":
                response = "Server stopped by user"
                conn.sendall(json.dumps(response).encode('utf8'))
                break
            if not data:
                response = "Server stopped without data"
                conn.sendall(json.dumps(response).encode('utf8'))
                break
