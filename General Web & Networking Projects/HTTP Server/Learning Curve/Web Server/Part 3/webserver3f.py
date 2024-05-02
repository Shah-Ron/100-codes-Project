##########################################################
#     Webserver3f.py - Dealing with the errno error      #
##########################################################

import socket
import os
import time
import errno
import signal

SERVER_ADDRESS = (HOST, PORT) = "", 8888
REQUEST_QUEUE_SIZE = 5
PID = os.getpid()

def grim_reaper(signum, frame):
    pid, status = os.wait()
    print("The Child process {pid} is terminating with status {status}".format(pid = pid, status = status))

def request_handler(client_connection):

    request = client_connection.recv(1024)
    print(request.decode('utf-8'))
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World! I dealt with the Zombieeeeeesssss!!!!
"""
    client_connection.sendall(http_response)
    time.sleep(60)

def server_forever():

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print("Serving in the port {PORT}".format(PORT = PORT))
    print("The Parent PID : {PID}".format(PID = PID))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args

            #restart 'accept' if it was interrupted
            if code == errno.EINTR:
                continue
            else:
                raise
        
        pid = os.fork()

        if pid == 0:
            listen_socket.close()
            request_handler(client_connection)
            client_connection.close()
            os._exit(0)
        else:
            client_connection.close()

if __name__ == "__main__":
    server_forever()
