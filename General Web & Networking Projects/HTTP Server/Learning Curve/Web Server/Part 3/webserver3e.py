#########################################################
#   webserver3e.py - Introducing Single Child running   #
#########################################################

import socket
import signal
import os
import time

SERVER_ADDRESS = (HOST, PORT) = "", 8888
REQUEST_SERVER_QUEUE = 5
PID = os.getpid()

def grim_reaper(signum, frame):
    pid, status = os.wait()
    print("Child {pid} is terminated with {status}"
          "\n".format(pid = pid, status = status)
    )

def request_handler(client_connection):
    
    request = client_connection.recv(1024)
    print(request.decode('utf-8'))
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World! I will make you wait you zombie child processssesssss!!!!!
"""
    client_connection.sendall(http_response)
    time.sleep(60)

def serve_forever():

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_SERVER_QUEUE)
    print(f"Serving the port {PORT}")
    print(f"The Parent PID (PPID): {PID}")

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        client_connection, client_address = listen_socket.accept()
        pid = os.fork()
        if pid == 0:
            listen_socket.close()
            request_handler(client_connection)
            client_connection.close()
            os._exit(0)
        else:
            client_connection.close()

if __name__ == "__main__":
    serve_forever()