import socket   # To create sockets
import time     # To make a client request sleep after one request
import os       # To fork it into child processes
import signal   # To avoid zombies
import errno    # to deal with zombie errors

SERVER_ADDRESS = (HOST, PORT) = "", 8888
REQUEST_QUEUE_SIZE = 5
PID = os.getpid()

def grim_reaper(signum, frame):
    """
    Kills the zombies by making them wait
    """
    while True:
        try:
            pid, status = os.waitpid(
                -1,             # Wait for child processes
                os.WNOHANG      # Do not wait and return EWOULDBLOCK error
            )
        except OSError:
            return
    
        if pid == 0: # No more zombies
            return

def request_handler(client_connection):
    """
    This function handles the requests from the clients to the server
    """

    # Recieves the requests
    request = client_connection.recv(1024)
    # Prints the request
    print(request.decode('utf-8'))
    
    # The HTTP response to give for the client
    http_response = b"""\
HTTP/1.1 200 OK

Hey, y'all!!! This is a simple proper web server hosted on 127.0.0.1 on port 8888. I properly went throught the educational website as provided in the README.md file to achieve this feast. I'm so happy about it. I hope anyone looking at my repository can use this for their understanding as well.
"""

    # Sending the response to the client
    client_connection.sendall(http_response)
    # Putting the client on sleep before the next request
    time.sleep(60)

def server_forever():
    """
    The function which will listen to the clients and will fork it into child processes and Parent processes
    """

    # Create a listening socket
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Making the socket as reusable
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # BInding the host and port together
    listen_socket.bind(SERVER_ADDRESS)
    # Listening to the client requests
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    
    print("Serving on the port {PORT}".format(PORT=PORT))
    print("Parent PID (PPID) : {PID}".format(PID=PID))

    # Making the child processes wait so that zombies die out
    signal.signal(signal.SIGCHLD, grim_reaper)

    while True:
        try:
            client_connection, client_address = listen_socket.accept()
        except IOError as e:
            code, msg = e.args

            # Restart the "accept()" if it was interrupted
            if code == errno.EINTR:
                continue
            else:
                raise
        
        # Fork the process into child and parent processes

        pid = os.fork() 
        if pid == 0:                            # For child Processes    
            listen_socket.close()               # Closes the copy o the child
            request_handler(client_connection)  # Calls the function that handles the requests
            client_connection.close()           # Closes the connection
            os._exit(0)                         # Exits the process
        else:                                   # For Parent Processes
            client_connection.close()           # Closes the parent process inorder to avoid the creation of zombies

if __name__ == "__main__":
    server_forever()