#!/usr/bin/python3

"""
Description: A module that define a Client-Server Application with Serialization
"""

import json
import socket


HOST = "localhost"
PORT = 6789

def start_server():
    """
    The server function.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data_received = conn.recv(1024)
                    if not data_received:
                        break
                    json_data = data_received.decode("utf-8")
                    data = json.loads(json_data)
                    print("Received Dictionary from Client:")
                    print(data)
                    response_str = json.dumps(data)
                    response_bytes = response_str.encode("utf-8")
                    conn.sendall(response_bytes)
        except json.JSONDecodeError as je:
            print(f"Erreur de décodage JSON : {je}")
        except Exception as e:
            print("Unexpected error: {}".format(e))


def send_data(data):
    """
    The client function.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            json_str = json.dumps(data)
            data_to_send = json_str.encode("utf-8")
            s.sendall(data_to_send)
        except Exception as e:
            print("Unexpected error: {}".format(e))