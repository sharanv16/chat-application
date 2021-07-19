import socket
import threading


class Client:
    PORT = 5050
    HEADER = 64
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = '!disconnect'
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)

    def __init__(self,name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        self.messages = []
        receive_thread = threading.Thread(target=self.receive_messages).start()
        self.send(name)
        self.lock = threading.Lock()

    def receive_messages(self):
        while True:
            try:
                msg = self.client.recv(self.HEADER).decode(self.FORMAT)
                #print(msg)
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
            except Exception as e:
                print('EXCEPTION: ', e)
                break

    def send(self,msg):
        self.client.send(msg.encode(self.FORMAT))
        #  print(client.recv(HEADER).decode(FORMAT))
        if msg == '!disconnect':
            self.client.close()

    def get_messages(self):
        msgs_cpy = self.messages[:]
        self.lock.acquire()
        self.messages=[]
        self.lock.release()
        return msgs_cpy

    def disconnect(self):
        self.send('!disconnect')