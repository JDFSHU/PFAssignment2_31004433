import socket
from threading import Thread
from datetime import datetime


SERVER_HOST = "127.0.0.1"  # server's IP address
SERVER_PORT = 5002  # server's port
separator_token = "<SEP>"  # we will use this to separate the client name & message
s = socket.socket()  # initialize TCP socket
print(f"[Connecting] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))  # connect to the server
print("[Established] Connected.")
name = input("Enter your name: ")


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)


t = Thread(target=listen_for_messages)   # thread that listens for messages
t.daemon = True  # ends whenever the main thread ends
t.start()  # start the thread

while True:
    to_send = input(name + ": ")    # message inputs
    if to_send.lower() == 'q':  # quits if only selecting q
        print("Quitting Chat Application")
        break
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # add the datetime
    to_send = f"[{date_now}] {name}{separator_token}{to_send}"
    s.send(to_send.encode())  # finally, send the message
s.close()  # close the socket
