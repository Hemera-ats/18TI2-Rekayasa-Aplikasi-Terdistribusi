import socket #ip + port number pair, ip identifies hist
import select
from threading import Thread # use to allow multiple pieces of code to run concurrently
import os
import argparse

Server_host = "127.0.0.1"
Server_port = 8080
separator = "<SEP>" # we will use this to separate the client name & message
     
client_sockets = set()
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #True, reconnect

serverSocket.bind((Server_host, Server_port))

serverSocket.listen(5)
print(f"[*] Listening as {Server_host}:{Server_port}")

def listeningClient(cs): #take any message sent from client and broadcast it
    while True:
        try:
            # listening by recieving and decode
            msg = cs.recv(1024).decode()
        except Exception as e:
            # if client no longer connected remove
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            # if we received a message, replace the <SEP> (messager keep in touch) 
            msg = msg.replace(separator, ": ")
        for client_socket in client_sockets:
            # send the message
            client_socket.send(msg.encode())

while True:
    # server always listen for another client
    client_socket, client_address = serverSocket.accept()
    print(f"[+] {client_address} connected.")
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listeningClient, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()

# close client sockets
for cs in client_sockets:
    cs.close()
# close server socket
serverSocket.close()