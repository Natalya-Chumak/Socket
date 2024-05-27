'''
первый способ с отправкой одного сообщения
'''
# import socket
#
# client = socket.socket()
# hostname = '10.39.0.38'
# port = 12345
#
# client.connect((hostname, port))
#
# message_to_server = client.recv(1024)
# print(message_to_server.decode())
#
# user_message = input('Введи сообщение серверу: ')
# client.send(user_message.encode())

# '''
# второй способ с отправкой нескольких сообщений
# '''
# import socket
#
#
# client = socket.socket()
# hostname = '10.39.160.69'
# port = 12345
#
# client.connect((hostname, port))
#
# while True:
#
#     message_to_server = client.recv(1024)
#     print(message_to_server.decode())
#
#     user_message = input('Введи сообщение серверу: ')
#     if user_message == 'q':
#         client.send('подключение закрывается. до свидания'.encode())
#         client.close()
#         break
#     client.send(user_message.encode())

'''
третий способ 1 сервер много клиентов
'''
import socket
import threading


client = socket.socket()
hostname = '10.39.160.69'
port = 12345

client.connect((hostname, port))

while True:

    message_to_server = client.recv(1024)
    print(message_to_server.decode())

    user_message = input('Введи сообщение серверу: ')
    if user_message == 'q':
        client.send('подключение закрывается. до свидания'.encode())
        client.close()
        break
    client.send(user_message.encode())