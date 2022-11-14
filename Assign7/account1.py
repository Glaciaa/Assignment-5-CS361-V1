import pika
import time
import sys
from tkinter import *
from tkinter.ttk import *

window = Tk()

addFriend = Entry(window, width = 30)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='CS361 Message')

print("Enter a name or enter 'stop' to stop.")

messageToSend = ""

#while messageToSend != "stop":
#   messageToSend = input("Enter your friend's name: ")
#    if messageToSend == "stop" or messageToSend == "Stop":
#        break
#    else:
#        channel.basic_publish(exchange='', routing_key='CS361 Message', body=messageToSend)
#        print(" [x] sent 'A message from CS361'")

def getFriend():
    global addFriend
    friendName = addFriend.get()

    channel.basic_publish(exchange='', routing_key='CS361 Message', body=friendName)
    print(" [x] sent 'A message from CS361'")

    

while True:
    window.geometry('350x100')
    window.resizable(0, 0)

    #place entry field
    addFriend.place(x = 40, y = 50)

    #calls makeNote function to create a small note window when clicked
    addButton = Button(window, text = 'Add Friend', command = getFriend)
    addButton.place(x = 250, y = 48)
    
    window.mainloop()

    break
