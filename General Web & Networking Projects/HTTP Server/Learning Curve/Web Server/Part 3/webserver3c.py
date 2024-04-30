###############################################
#     Webserver3c.py - Concurrent server      # 
#                                             #
#   Child processes sleep for 60s after one   #
#                   request                   #
#                                             #
#  Parent and child processes close duplicate #
#                   descriptors               #
###############################################

import socket
import time
import os

SERVER_ADDRESS = (HOST,PORT) = "",8888
REQUEST_QUEUE_SIZE = 2
PID = os.getpid()

def request_handler(client_connection):
    """Function to handle the requests that are accepted"""
    # pid of child and parent processes
    pid = os.getpid()
    ppid = os.getppid()
    print(f"Child PID: {pid}, Parent PID: {ppid}")

    # Recieving the connection upto 1024 bytes
    request = client_connection.recv(1024)

    # Printing the decoded data from the request
    print(request.decode())

    # The response for the connection
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World! This is your friend Shahron!
"""
    # Sending the response
    client_connection.sendall(http_response)

    # Sleeping time to avoid failure of server
    time.sleep(60)

def server_forever():
    """Function to create a socket and listen to it"""

    # Create a listening socket
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Setting it for reusability
    listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # Binding the server address with port number
    listen_socket.bind(SERVER_ADDRESS)
    # Listening to the socket
    listen_socket.listen(REQUEST_QUEUE_SIZE)

    print(f"Serving throught the port {PORT} .... ")
    print(f"Parent PID (PPID) : {PID}\n")

    while True:
        
        # Gets the details about the client connection and the client address from the accepted the client
        client_connection, client_address = listen_socket.accept()
        # recieving the pid value
        pid = os.fork()

        if pid == 0: # For child processes
            listen_socket.close() # Close the child copy
            # Calls the request handler function
            request_handler(client_connection)
            # Closes the connection
            client_connection.close()
            os._exit(0) # Child processes end here
        else: # For Parent processes
            client_connection.close() # Close the parent copy and loop over for the next one
    
if __name__ == "__main__":
    server_forever()