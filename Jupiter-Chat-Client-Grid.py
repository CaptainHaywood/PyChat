
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


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
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")

jchat = tkinter.Label(messages_frame, text="Jupiter Chat", fg="orange", font=("TkDefaultFont", 20))
jchat.grid(row=0, column=0, sticky=tkinter.NW)

#sepA = tkinter.Seperator(messages_frame, orient=tkinter.HORIZONTAL)
#sepA.pack(side=tkinter.LEFT, anchor=tkinter.NW) #doesnt work fix

servb = tkinter.Button(messages_frame, text="Servers", width = 20)
servb.grid(row=0, column=0, sticky=tkinter.NW)

scrollbar = tkinter.Scrollbar(messages_frame)  #scrollbar (vertical)
#holds msgs
msg_list = tkinter.Listbox(messages_frame, height=30, width=100, yscrollcommand=scrollbar.set)
scrollbar.grid(row=0, column=2)
msg_list.grid(row=0, column=1)
msg_list.grid()
messages_frame.grid()

send_button = tkinter.Button(top, text="Send", command=send)
send_button.grid(row=1, column=1)
entry_field = tkinter.Entry(top, width = 95, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.grid(row=1, column=0)


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
