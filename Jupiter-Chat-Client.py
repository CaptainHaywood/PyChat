from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

def about():
    def aboutclose():
        aboutwin.destroy()

    aboutwin = tkinter.Tk()
    aboutwin.title("About")
    jchat = tkinter.Label(aboutwin, text="JUPITER CHAT", fg="orange", font=("TkDefaultFont", 15))
    jchat.grid(row=0, column=0, sticky=tkinter.N)
    vers = tkinter.Label(aboutwin, text="v1.0.0")
    vers.grid(row=1, column=0, sticky=tkinter.N)
    cright = tkinter.Label(aboutwin, text="A Python-based IRC-alike chat program using Tkinter and sockets.")
    cright.grid(row=2, column=0, sticky=tkinter.N)
    cright = tkinter.Label(aboutwin, text="© James Haywood 2018")
    cright.grid(row=3, column=0, sticky=tkinter.N)
    leaveabout = tkinter.Button(aboutwin, text="Close", width=10, command=aboutclose)
    leaveabout.grid(row=4, column=0, sticky=tkinter.S)



def servers():
    print("")

def settings():
    print("")

def helpb():
    def helpclose():
        helpwin.destroy()

    helpwin=tkinter.Tk()
    helpwin.title("Help")
    helptitle = tkinter.Label(helpwin, text="HELP", fg="blue", font=("TkDefaultFont", 15))
    helptitle.grid(row=0, column=0, sticky=tkinter.N)
    

def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  #client may have left the chat
            break


def send(event=None):
    msg = my_msg.get()
    my_msg.set("")
    client_socket.send(bytes(msg, "utf8"))
    if msg == "/leave":
        client_socket.close()
        top.destroy()
        top.quit()



def on_closing(event=None):
    my_msg.set("/leave")
    send()

top = tkinter.Tk()
top.title("Jupiter Chat")

messages_frame = tkinter.Frame(top)
buttons_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")

jchat = tkinter.Label(buttons_frame, text="MENU", fg="blue", font=("TkDefaultFont", 20))
jchat.grid(row=0, column=3, sticky=tkinter.N)

#sepA = tkinter.Seperator(messages_frame, orient=tkinter.HORIZONTAL)
#sepA.pack(side=tkinter.LEFT, anchor=tkinter.NW) #doesnt work fix

servb = tkinter.Button(buttons_frame, text="Servers", width = 20, command=servers)
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
entry_field = tkinter.Entry(top, width = 100, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.grid(row=2, column=0)


top.protocol("WM_DELETE_WINDOW", on_closing)

HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.
