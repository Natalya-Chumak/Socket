#UPD
#HTTP - 81, порт, который использует браузер

'''
первый способ с отправкой одного сообщения
'''
# import socket
#
#
# server = socket.socket()
# hostname = '10.39.160.69'     # socket.gethostname() 'localhost' '127.0.0.1'
# port = 12345                        #65535
# server.bind((hostname, port))
#
# server.listen(5)
# print('server is started')
#
# connection, adress = server.accept()
# print('someone connected!')
# print(connection)
# print(adress)
# connection.send('hi, new client. Привет, клиент'.encode()) #превращаем в байт-строку
# user_message = connection.recv(1024)
# print(user_message.decode())

# '''
# второй способ с отправкой нескольких сообщений
# '''
#
# import socket
#
#
# server = socket.socket()
# hostname = '10.39.160.69'     # socket.gethostname() 'localhost' '127.0.0.1'
# port = 12345                        #65535
# server.bind((hostname, port))
#
# server.listen(5)
# print('server is started')
#
# connection, adress = server.accept()
# print('someone connected!')
# print(connection)
# print(adress)
#
# while True:
#     server_message = input('Сообщение клиенту: ')
#     if server_message == 'q':
#         connection.send('подключение закрывается. до свидания'.encode())
#         connection.close()
#         break
#     connection.send('hi, new client. Привет, клиент'.encode()) #превращаем в байт-строку
#     user_message = connection.recv(1024)
#     print(user_message.decode())


'''
третий способ 1 сервер много клиентов
'''

import socket
import threading


def listen_client_messages(connection):
    pass


server = socket.socket()
hostname = '10.39.160.69'     # socket.gethostname() 'localhost' '127.0.0.1'
port = 12345                        #65535
server.bind((hostname, port))

server.listen(5)
print('server is started')

all_clients = set()



while True:
    connection, adress = server.accept()
    print('someone connected!')
    print(connection)
    print(adress)
    all_clients.add(connection)






    server_message = input('Сообщение клиенту: ')
    if server_message == 'q':
        connection.send('подключение закрывается. до свидания'.encode())
        connection.close()
        break
    connection.send('hi, new client. Привет, клиент'.encode()) #превращаем в байт-строку
    user_message = connection.recv(1024)
    print(user_message.decode())
