import sys
import os

print(sys.stdin)

print(sys.stdin.fileno())

print(sys.stdout.fileno())

print(sys.stderr.fileno())

data = 'hello\n'.encode("utf-8")

res = os.write(sys.stdout.fileno(), data)
print(res)

import socket

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(listen_socket.fileno())