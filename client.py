import socket
import threading
import time

PORT = 5050
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!disconnect'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

messages = []


def send(msg):
    client.send(msg.encode(FORMAT))
#  print(client.recv(HEADER).decode(FORMAT))
    if msg == '!disconnect':
        print(client.recv(HEADER).decode(FORMAT))
        client.close()


def receive_messages():
    while True:
        try:
            msg = client.recv(HEADER).decode(FORMAT)
            messages.append(msg)
            print(msg)
        except Exception as e:
            print('EXCEPTION: ',e)
            break


receiveThread = threading.Thread(target=receive_messages).start()

print("to disconnect type '!disconnect'")
print("TYPE YOUR Name:")
send('sharan')
time.sleep(5)
send('hello')
time.sleep(5)
send('!disconnect')


