import socket

# Creating a socket and connecting it to the server

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8888))

# Sending and recieving some data

host, port = sock.getsockname()[:2]
sock.sendall(b'Shahron')
data = sock.recv(1024)
print(data.decode())
print(host, port)