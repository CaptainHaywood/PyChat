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
global silenceon
global space
space = ": "
silenceon = "no"

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
        client.send(bytes(welcome, "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):
    global silenceon
    name = client.recv(BUFSIZ).decode("utf8")
    welcomeM = success
    client.send(bytes(welcomeM, "utf8"))
    msg = "%s has joined the chat." % name
    broadcast(bytes(msg, "utf8"))
    client.send(bytes(" ", "utf8"))
    clients[client] = name

    def broadcaster():
        client.send(bytes("Please enter the broadcast message.", "utf8"))
        bmsg = client.recv(BUFSIZ).decode("utf8")
        msg = servername + space + bmsg
        broadcast(bytes(msg, "utf8"))
    
    while True:
        msg = client.recv(BUFSIZ)
        if msg == bytes("/leave", "utf8"):
            #client.send(bytes("/leave", "utf8")) # THIS FUCKS UP THE DISCON SEQUENCE
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break
        
        elif msg == bytes("/cloak", "utf8"):
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            
        elif msg == bytes("/uncloak", "utf8"):
            broadcast(bytes("%s has joined the chat." % name, "utf8"))
            
        elif msg == bytes("/clear", "utf8"):
            uselessvarforthing = "AAAAA"

        elif msg == bytes("/name", "utf8"):
            client.send(bytes("Please enter your new name.", "utf8"))
            name = client.recv(BUFSIZ).decode("utf8")
            client.send(bytes("Name changed!", "utf8"))
            msg = "%s has changed their name." % name
            broadcast(bytes(msg, "utf8"))
            
        elif msg == bytes("/silence", "utf8"):
            client.send(bytes("Please enter admin PIN.", "utf8"))
            sentpin = client.recv(BUFSIZ).decode("utf8")
            if sentpin == adPIN:
                broadcast(bytes("Silence is now active. No messages will go through until Silence is deactivated.", "utf8"))
                silenceon = "yes"
            else:
                client.send(bytes("Invalid PIN!", "utf8"))

        elif msg == bytes("/noise", "utf8"):
            client.send(bytes("Please enter admin PIN.", "utf8"))
            sentpin = client.recv(BUFSIZ).decode("utf8")
            if sentpin == adPIN:
                broadcast(bytes("Silence has been deactivated. Messages will now go through.", "utf8"))
                silenceon = "no"
            else:
                client.send(bytes("Invalid PIN!", "utf8"))

        elif msg == bytes("/broadcast", "utf8"):
            client.send(bytes("Please enter admin PIN.", "utf8"))
            sentpin = client.recv(BUFSIZ).decode("utf8")
            if sentpin == adPIN:
                broadcaster()
            else:
                client.send(bytes("Invalid PIN!", "utf8"))


        else:
            broadcast(msg, name+": ")


def broadcast(msg, prefix=""):  # prefix is for name identification.
    global silencon
    """Broadcasts a message to all the clients."""
    if silenceon == "no":
        for sock in clients:
            sock.send(bytes(prefix, "utf8")+msg)
    else:
        uselessvarwoo = "ZZZ"



        
clients = {}
addresses = {}

HOST = ''
PORT = sport #33000 default
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
