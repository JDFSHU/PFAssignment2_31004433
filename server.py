import socket
from threading import Thread


SERVER_HOST = "127.0.0.1"  # server's IP address
SERVER_PORT = 5002  # server port (obviously)
separator_token = "<SEP>"  # we will use this to separate the client name & message
client_sockets = set()  # initialize all connected client's sockets
s = socket.socket()  # create a TCP socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # make the port as reusable port
s.bind((SERVER_HOST, SERVER_PORT))  # bind the socket to the address we specified
s.listen(5)  # listen for upcoming connections
print(f"[Chat Server] Listening on socket: {SERVER_HOST}:{SERVER_PORT}")


def listen_for_client(cs):
    while True:
        try:

            msg = cs.recv(1024).decode()  # keep listening for a message
        except Exception as e:
            print(f"[Attention] Error: {e}")  # client no longer connected
            client_sockets.remove(cs)  # remove it from the set
        else:
            msg = msg.replace(separator_token, ": ")  # if we received a message, replace the <SEP>

            for client_socket in client_sockets:  # iterate over all connected sockets
                # and send the message
                client_socket.send(msg.encode())


while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()
    print(f"[New Chat Client] {client_address} connected.")
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()

# for some reason pycharm says this is unreachable, however it is. Moving it/Deleting it in anyway breaks the app
for cs in client_sockets:  # close client sockets
    cs.close()
s.close()  # close server socket
