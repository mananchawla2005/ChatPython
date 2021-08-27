import threading
import socket

nickname = input('Enter a valid nickname ')
import sys

from time import sleep

words = f'Hello {nickname} welcome to my chat application. \n I hope you will like it! \n For connecting to the server enter ip and the port \n to connect to. \n For further info type /help \n'
for char in words:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Enter the ip address of the remote server: ")
port = int(input("Enter the connection port: "))


try:
    client.connect((host, port))
except:
    print("Error connecting to the server. Is it up? Please check the ip address and the port and try again.")

def recieve():
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            if(msg=='NICK'):
                client.send(nickname.encode('ascii'))
            elif(msg=='BANNED'):
                client.close()    
            elif(msg=='KICKED'):
                client.close()           
            else:
                print(msg)
        except:
            print('Unexpected Error! Connection Closed....')
            print('Press any key to continue.....')
            client.close()
            break

def write():
    global recieve_thread
    global write_thread
    while True:
        message = input("")
        if(message=="/help"):
            print("Welcome to Chatting Application!!")
            print("Here are some basic commmands to start with: ")
            print("/help:     Prints the help menu")
            print("/about:    Shows the app information")
            print("/dc:       Disconnects from the server!")
            print("/ban:      Bans the person(privelaged command)")
            print("/unban:    Unbans the person(privelaged command)")
            print("/kick:     Kicks the person(privelaged command)")
        elif(message=="/about"):
            print('Created by Manan Chawla')
            print('-------------------------')
            print('The program is made using websockets.')
            print('Working: ')
            print('Server listens on a specific port. Whenever a client wants to connect to the server, ')
            print('It sends a tcp request to the server and then server connects the client.')
            print('Additional logging is made possible by file handling')
        elif(message=="/dc"):
            print('Disconnecting from server and closing the program.......')
            print('Press any key to continue.....')
            client.close()
        else:
            msg = f'{nickname}: {message}'
            client.send(msg.encode('ascii'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()