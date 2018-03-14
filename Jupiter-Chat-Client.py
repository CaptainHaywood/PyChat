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
    my_msg.set("")  #clear box
    client_socket.send(bytes(msg, "utf8"))
    if msg == "/leave":
        client_socket.close()
        top.quit()
    elif msg == "/help":
        helpA = "---HELP MENU---"
        helpB = "/help ~ This help menu."
        helpC = "/leave ~ Leave the chatroom."
        msg_list.insert(tkinter.END, helpA)
        msg_list.insert(tkinter.END, helpB)
        msg_list.insert(tkinter.END, helpC)
        


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("/leave")
    send()

top = tkinter.Tk()
top.title("Jupiter Chat")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=30, width=100, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

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
