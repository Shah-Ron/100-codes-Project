############################################################
#     Webserver3d.py - Parent Connection Left Unclosed     #
############################################################

import socket
import time
import os

SERVER_ADDRESS = (HOST, PORT) = "", 8888
REQUEST_QUEUE_SIZE = 5
PID = os.getpid()

def request_handler(client_connection):

    request = client_connection.recv(1024)
    print(request.decode('utf-8'))
    http_response = b"""\
HTTP/1.1 200 OK

Hello World. Creating Zombies is my aim!!!!!!!!!!!! (PS: Zombie programs, please don't be alert)
"""
    client_connection.sendall(http_response)
    time.wait(60)

def server_forever():

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print(f"Serving on the prot {PORT}")

    clients = []

    while True:
        client_connection, client_address = listen_socket.accept()
        clients.append(client_connection)
        pid = os.fork()
        if pid == 0:
            listen_socket.close()
            request_handler(client_connection)
            client_connection.close()
            os._exit(0)
        else:

            # Commenting the client_connection.close() inorder to show the working of zombies
            #client_connection.close()
            print(len(clients))
        
if __name__ == "__main__":
    server_forever()