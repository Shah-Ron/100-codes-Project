############################################
#    Iterative Server - webserver3a.py     #
############################################

import socket

SERVER_ADDRESS = (Host,Port) = "", 8888
REQUEST_QUEUE_SIZE = 3

def handle_request(client_connection):
    """Handles all the request"""

    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b"""\
HTTP/1.1 200 OK

Hello World! This is my Tryout! I will succeed at this damn thing! Never back down!
"""
    client_connection.sendall(http_response)

def server_forever():
    """Describes the initialising part and the server"""

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print(f"Serving HTTP on port {Port} .....")

    while True:
        client_connection, client_address = listen_socket.accept()
        handle_request(client_connection)
        client_connection.close()

if __name__ == "__main__":
    server_forever()