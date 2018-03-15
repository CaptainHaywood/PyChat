from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import shelve

global motdN
global motdA
global motdB
global motdC
global motdD
global motdE
global welcome
global success
global servername
global maxconn
global logonM
global adPIN
global sport

shelfFile = shelve.open('server_config')
motdN = shelfFile ['motdN_Var']
motdA = shelfFile ['motdA_Var']
motdB = shelfFile ['motdB_Var']
motdC = shelfFile ['motdC_Var']
motdD = shelfFile ['motdD_Var']
motdE = shelfFile ['motdE_Var']
welcome = shelfFile ['welcome_Var']
success = shelfFile ['success_Var']
servername = shelfFile ['servername_Var']
maxconn = shelfFile ['maxconn_Var']
logonM = shelfFile ['logonM_Var']
adPIN = shelfFile ['adPIN_Var']
sport = shelfFile ['sport_Var']
shelfFile.close()

def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes(welcome, "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    name = client.recv(BUFSIZ).decode("utf8")
    welcomeM = success
    client.send(bytes(welcomeM, "utf8"))
    msg = "%s has joined the chat." % name
    broadcast(bytes(msg, "utf8"))
    client.send(bytes(" ", "utf8"))
    print("")
    client.send(bytes(motdN, "utf8")) #try and fix MOTD sending
    print("")
    client.send(bytes(motdA, "utf8"))
    print("")
    client.send(bytes(motdB, "utf8"))
    print("")
    client.send(bytes(motdC, "utf8"))
    print("")
    client.send(bytes(motdD, "utf8"))
    print("")
    client.send(bytes(motdE, "utf8"))
    print("")
    client.send(bytes(motdN, "utf8"))
    print("")
    client.send(bytes(" ", "utf8"))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("/leave", "utf8"):
            if msg != bytes("/help", "utf8"):
                broadcast(msg, name+": ")
        else:
            if msg == bytes("/leave", "utf8"):
                client.send(bytes("/leave", "utf8"))
                client.close()
                del clients[client]
                broadcast(bytes("%s has left the chat." % name, "utf8"))
                break
            else:
                print ("A-OK")


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = ''
PORT = 33000 #33000 default
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(maxconn)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
