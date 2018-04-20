from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import shelve

global welcome
global success
global servername
global maxconn
global logonM
global adPIN
global sport

shelfFile = shelve.open('server_config')
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
        client.send(bytes(welcome, "unicode"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    name = client.recv(BUFSIZ).decode("unicode")
    welcomeM = success
    client.send(bytes(welcomeM, "unicode"))
    msg = "%s has joined the chat." % name
    broadcast(bytes(msg, "unicode"))
    client.send(bytes(" ", "unicode"))
    clients[client] = name
    
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("/leave", "unicode"):
            broadcast(msg, name+": ")
        else:
            #client.send(bytes("/leave", "unicode")) # THIS FUCKS UP THE DISCON SEQUENCE
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "unicode"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "unicode")+msg)

        
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
