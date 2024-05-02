#######################################################################################################
#    webserver3g.py - Dealing with error that rises when 128 simultaneous client request are done     #
#######################################################################################################

import socket
import time
import os
import signal
import errno

SERVER_ADDRESS = (HOST, PORT) = "", 8888
REQUEST_QUEUE_SIZE = 5
PID = os.getpid()

def grim_reaper(signum, frame):
    while True:
        try:
            pid, status = os.waitpid(
                -1,             # Wait for child process
                os.WNOHANG      # Do not block and return EWOULDBLOCK error
            )
        except OSError:
            return
        
        if pid == 0:            # This means no more zombies
            return

def request_handler(client_connection):
    request = client_connection.recv(1024)
    print(request.decode('utf-8'))
    http_response = b"""\
HTTP/1.1 200 OK

Hello World, I successfully dealt with the 128 zombies as well
"""
    client_connection.sendall(http_response)
    time.sleep(60)

def serve_forever():

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)

    print("Serving in the port {PORT}".format(PORT = PORT))
    print("Parent PID (PPID): {PID}".format(PID = PID))

    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msgs = e.args

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
    serve_forever()