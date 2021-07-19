import socket
import threading
import time
from person import Person


PORT = 5050
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!disconnect'
SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)
MAX_CONNECTION = 10

participants = []


# creating a socket
ADDR = (SERVER,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)


def broadcast(msg,name):
    for person in participants:
        client = person.client
        try:
            client.send(msg.encode(FORMAT))
        except Exception as e:
            print("EXCEPTION: ",e)


def handle_client(person):
    client = person.client
    set_name = False
    connected = True
    while connected:
        msg = client.recv(HEADER).decode(FORMAT)
#        client.send("[SYSTEM]:MESSAGE RECEIVED".encode(FORMAT))
# set person name
        if set_name is False:
            person.set_name(msg)
            broadcast(f'{person.name} has joined the chat',"")
            set_name = True
        else:
            if msg == DISCONNECT_MESSAGE:
                client.close()
                participants.remove(person)
                broadcast(f"{person.name} has disconnected","")
                connected = False
            else:
                print(f"{person.name}: {msg}")
                broadcast(f"{person.name}: "+msg,person.name)


def wait_connection():
    while True:
        client, addr = server.accept()
        person = Person(addr,client)
        participants.append(person)
        print(f"{addr} has connected")
        print(f"No  of Active Conections = {threading.activeCount()-1}")
        startThread = threading.Thread(target=handle_client,args=(person,))
        startThread.start()


if __name__ == "__main__":
    print("[SERVER HAS STARTED]....")
    server.listen(MAX_CONNECTION)
    print("SERVER IS WAITING FOR CONNECTIONS....")
    wait_thread = threading.Thread(target=wait_connection)
    wait_thread.start()
    wait_thread.join()
    server.close()

