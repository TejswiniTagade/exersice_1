import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("192.168.43.52", 1234))

s.listen(10)
c, addr = s.accept()
print("Connected")

