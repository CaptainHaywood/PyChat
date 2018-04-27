from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
import tkinter
import shelve
from tkinter import ttk
from pygame import mixer
global HOST
global PORT
global conecc
global host_entry
global port_entry
global client_socket


HOST = "OFFLINE"
PORT = "OFFLINE"
startup = "no"
conecc = "NO"
mixer.init(frequency=22050, size=-16, channels=3, buffer=4096)


def settings():
    
    def settingsclose():
        setwin.destroy()
        
    def getsetvars():

        setwin.destroy()
        

    notificationset = tkinter.IntVar()
    setwin = tkinter.Tk()
    setwin.title("Settings")
    soundlabel = tkinter.Label(setwin, text="Sound")
    soundlabel.grid(row=0, column=0)

    funclabel = tkinter.Label(setwin, text="Functional")
    funclabel.grid(row=0, column=1)

    saveclose = tkinter.Button(setwin, text="Save and Close", command = getsetvars)
    saveclose.grid(row=0, column=2)
    nosaveclose = tkinter.Button(setwin, text="Close Without Saving", command = settingsclose)
    nosaveclose.grid(row=1, column=2)
    

def about():
    def aboutclose():
        aboutwin.destroy()

    aboutwin = tkinter.Tk()
    aboutwin.title("About")
    jchat = tkinter.Label(aboutwin, text="PyChat", fg="blue", font=("TkDefaultFont", 15))
    jchat.grid(row=0, column=0, sticky=tkinter.N)
    vers = tkinter.Label(aboutwin, text="v1.0.0")
    vers.grid(row=1, column=0, sticky=tkinter.N)
    cright = tkinter.Label(aboutwin, text="A Python-based IRC-alike chat program using Tkinter and sockets.")
    cright.grid(row=2, column=0, sticky=tkinter.N)
    cright = tkinter.Label(aboutwin, text="© James Haywood 2018")
    cright.grid(row=3, column=0, sticky=tkinter.N)
    leaveabout = tkinter.Button(aboutwin, text="Close", width=10, command=aboutclose)
    leaveabout.grid(row=4, column=0, sticky=tkinter.S)

def connect():
    global conecc
    global client_socket
    global HOST
    global PORT
    PORT = int(PORT)
    def cerrors():
        cerror.destroy()
    
    try:
        BUFSIZ = 1024
        ADDR = (HOST, PORT)
        
        client_socket = socket(AF_INET, SOCK_STREAM)
            
        client_socket.connect(ADDR)

        receive_thread = Thread(target=receive) 
        receive_thread.start()
        conecc = "YES"
        
        
    except:
        cerror = tkinter.Tk()
        cerror.title("ERROR")
        cerrorl = tkinter.Label(cerror, text="ERROR", fg="red", font=("TkDefaultFont", 15))
        cerrorl.grid(row=0, column=0)
        cerrore = tkinter.Label(cerror, text="PyChat could not connect to that server. It may be at capacity, or offline.")
        cerrore.grid(row=1, column=0)
        cerrorf = tkinter.Label(cerror, text="Contact the operator of the server or try again later.")
        cerrorf.grid(row=2, column=0)
        cerrorc = tkinter.Button(cerror, text="OK", width=5, command=cerrors)
        cerrorc.grid(row=3, column=0)
        
        

def disconnect():
    HOST = "OFFLINE"
    PORT = "OFFLINE"
    my_msg.set("/leave")
    send()

def servers():
    global HOST
    global PORT

    def refresh():
        serverwin.destroy()
        servers()
    
    def serverclose():
        serverwin.destroy()

    def connectvars():
        global HOST
        global PORT
        HOST = host_entry.get()
        PORT = port_entry.get()
        connect()
    
    hostv = tkinter.StringVar()
    portv = tkinter.StringVar()
    chost = tkinter.StringVar()
    serverwin = tkinter.Tk()
    serverwin.title("Manage Connections")
    currentcon = tkinter.Label(serverwin, text="Current Connection")
    currentcon.grid(row=1, column=1)
    currenthostl = tkinter.Label(serverwin, text=HOST)
    currentportl = tkinter.Label(serverwin, text=PORT)
    currenthostl.grid(row=2, column=1)
    currentportl.grid(row=3, column=1)
    seperatorserver = tkinter.Label(serverwin, text=" ")
    seperatorserver.grid(row=4, column=2)
    currenthost = tkinter.Label
    hostlabel = tkinter.Label(serverwin, text="Host IP:")
    hostlabel.grid(row=1, column=2)
    portlabel = tkinter.Label(serverwin, text="Port:")
    portlabel.grid(row=2, column=2)
    host_entry = tkinter.Entry(serverwin, width = 25, textvariable=hostv)
    host_entry.grid(row=1, column=3)
    port_entry = tkinter.Entry(serverwin, width = 25, textvariable=portv)
    port_entry.grid(row=2, column=3)
    refreshb = tkinter.Button(serverwin, width=10, text="Refresh", command=refresh)
    refreshb.grid(row=5, column=1)
    connectb = tkinter.Button(serverwin, width=10, text="Connect", command=connectvars)
    connectb.grid(row=5, column=3)
    closeb = tkinter.Button(serverwin, text="Close", command=serverclose)
    closeb.grid(row=5, column=2)
    
    


def helpb():
    def helpclose():
        helpwin.destroy()

    helpwin=tkinter.Tk()
    helpwin.title("Help")
    helptitle = tkinter.Label(helpwin, text="HELP", fg="blue", font=("TkDefaultFont", 15))
    helptitle.grid(row=0, column=0, sticky=tkinter.N)
    help_list = tkinter.Listbox(helpwin, height=10, width=75)
    help_list.grid(row=1, column=0)
    help_list.insert(tkinter.END, "GENERAL COMMANDS")
    help_list.insert(tkinter.END, "/leave: Leave the server you are currently connected to.")
    help_list.insert(tkinter.END, "/cloak: Broadcast that you have left the chat, but remain connected.")
    help_list.insert(tkinter.END, "/uncloak: Broadcast that you have rejoined the chat.")
    help_list.insert(tkinter.END, "/clear: Clear the message window.")
    help_list.insert(tkinter.END, "/name: Change your name.")
    help_list.insert(tkinter.END, "")
    help_list.insert(tkinter.END, "ADMINISTRATOR COMMANDS")
    help_list.insert(tkinter.END, "PIN REQUIRED")
    help_list.insert(tkinter.END, "/silence: Prevents any conversation from happening.")
    help_list.insert(tkinter.END, "/noise: Disables /silence if active; otherwise does nothing.")
    help_list.insert(tkinter.END, "/broadcast: Enter a message to be broadcast anonymously.")
    help_list.insert(tkinter.END, "/close: Broadcast a warning and close the server after ten seconds.")
    helpcb = tkinter.Button(helpwin, text="Close", width=10, command=helpclose)
    helpcb.grid(row=2, column=0, sticky=tkinter.S)





def receive():
    while True:
        try:
            if conecc == "YES":
                msg = client_socket.recv(BUFSIZ).decode("utf8")
                msg_list.insert(tkinter.END, msg)
                mixer.Channel(0).play(mixer.Sound('message.ogg'))
            else:
                uselessvar = "AAAAA"
        except OSError:  #client may have left the chat
            break


def send(event=None):
    global conecc
    global client_socket
    if conecc == "NO":
        msg_list.insert(tkinter.END, "OFFLINE")
    else:
        msg = my_msg.get()
        my_msg.set("")
        client_socket.send(bytes(msg, "utf8"))
        if msg == "/leave":
            msg_list.insert(tkinter.END, "")
            msg_list.insert(tkinter.END, "DISCONNECTED FROM SERVER")
            client_socket.close()
            del client_socket
            conecc = "NO"
            #top.destroy()
            #top.quit()
        elif msg == "/clear":
            msg_list.delete(0, tkinter.END)
            
        


def on_closing(event=None):
    my_msg.set("/leave")
    send()
    top.destroy()

top = tkinter.Tk()
top.title("PyChat")

messages_frame = tkinter.Frame(top)
buttons_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")

jchat = tkinter.Label(buttons_frame, text="MENU", fg="blue", font=("TkDefaultFont", 20))
jchat.grid(row=0, column=3, sticky=tkinter.N)

#sepA = tkinter.Seperator(messages_frame, orient=tkinter.HORIZONTAL)
#sepA.pack(side=tkinter.LEFT, anchor=tkinter.NW) #doesnt work fix

servb = tkinter.Button(buttons_frame, text="Connections", width = 20, command=servers)
servb.grid(row=0, column=1, sticky=tkinter.NW)

helpb = tkinter.Button(buttons_frame, text="Help", width = 20, command=helpb)
helpb.grid(row=0, column=2, sticky=tkinter.NW)

settb = tkinter.Button(buttons_frame, text="Settings", width = 20, command=settings)
settb.grid(row=0, column=4, sticky=tkinter.NE)

aboutb = tkinter.Button(buttons_frame, text="About", width = 20, command=about)
aboutb.grid(row=0, column=5, sticky=tkinter.NE)

scrollbar = tkinter.Scrollbar(messages_frame)  #scrollbar (vertical)
#holds msgs
msg_list = tkinter.Listbox(messages_frame, height=30, width=100, yscrollcommand=scrollbar.set)
scrollbar.grid(row=1, column=2, sticky=tkinter.E)
msg_list.grid(row=1, column=1)
msg_list.grid()
buttons_frame.grid()
messages_frame.grid()

#send_button = tkinter.Button(top, text="Send", command=send)
#send_button.grid(row=2, column=1, sticky=tkinter.SE)
#Above code clusterfucks the UI, DO NOT UNCOMMENT UNDER ANY CIRCUMSTANCES

entry_field = tkinter.Entry(top, width = 100, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.grid(row=2, column=0)
                                  
top.protocol("WM_DELETE_WINDOW", on_closing)

#HOST = input('Enter host: ')
#PORT = input('Enter port: ')
#if not PORT:
#    PORT = 33000
#else:
#    PORT = int(PORT)

#HOST = "LOCALHOST"
#PORT = 33000

BUFSIZ = 1024
#ADDR = (HOST, PORT)

#client_socket = socket(AF_INET, SOCK_STREAM)
#client_socket.connect(ADDR)

#receive_thread = Thread(target=receive)
#receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.
