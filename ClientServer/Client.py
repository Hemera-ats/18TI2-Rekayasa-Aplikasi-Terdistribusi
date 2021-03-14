import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

# init colors
init()

colorsMessage = [Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX, Fore.RED, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW]

# choose a random color for the client
client_color = random.choice(colorsMessage)

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8080 # server's port
separator = "<SEP>" # we will use this to separate the client name & message

# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

# prompt the client for a name
name = input("Enter your name: ")

def listeningMessages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

# thread to listens for messages from client & print them
t = Thread(target=listeningMessages)
# make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()

while True:
    # input message we want to send to the server
    to_send =  input()
    # to break the connection
    if to_send.lower() == 'end':
        break
    # add the datetime, name & the color of the sender
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"{client_color}[{date_now}] {name}{separator}{to_send}{Fore.RESET}"
    # finally, send the message
    s.send(to_send.encode())

# close the socket
s.close()