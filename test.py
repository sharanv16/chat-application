from clientclass import Client
import threading
import time

c1=Client("sharan")
time.sleep(2)
c2=Client("smiron")
time.sleep(2)


def update_messages():
    msgs=[]
    run = True
    while run:
        time.sleep(0.1)
        new_messages=c1.get_messages()
        msgs.extend(new_messages)
        for msg in new_messages:
            print(msg)
            if msg == '!disconnect':
                run = False
                break


threading.Thread(target=update_messages).start()

c1.send("hello")
time.sleep(2)
c2.send("hi")
time.sleep(1)
c1.disconnect()
time.sleep(1)
c2.disconnect()