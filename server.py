#UPD
#HTTP - 81, порт, который использует браузер
import socket


server = socket.socket()
hostname = socket.gethostname()     #'localhost' '127.0.0.1'
server.bind(hostname, 12345)
