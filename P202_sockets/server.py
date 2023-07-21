import json
import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 65432
VERSION = str(f"Server at host {HOST} working on port {PORT}. Software version 1.0")
start_time = datetime.now()
print(start_time)


def getServerTime():
    global start_time
    time_now = datetime.now()
    return time_now - start_time


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
                response = str(getServerTime())
                conn.sendall(json.dumps(response).encode('utf8'))
            if data == "help":
                response = "Commands to use: uptime, info, help, stop"
                conn.sendall(json.dumps(response).encode('utf8'))
            if data == "stop":
                response = "Server stopped by user"
                conn.sendall(json.dumps(response).encode('utf8'))
                break
            if not data:
                response = "Server stopped without data"
                conn.sendall(json.dumps(response).encode('utf8'))
                break
