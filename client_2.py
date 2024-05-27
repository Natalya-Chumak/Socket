import socket
import threading


client = socket.socket()
hostname = '10.39.160.69'
port = 12346

client.connect((hostname, port))
user_name = input('Введите имя: ')
client.send(user_name.encode())

while True:


    user_message = input('Введи сообщение серверу(quit для выхода): ')
    if user_message == 'q':
        print('Вы отключены от чата')
        client.send('quit'.encode())
        client.close()
        break
    client.send(user_message.encode())