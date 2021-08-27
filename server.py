import threading
import sys
import socket

host = input("Enter the ip address of this server: ")
port = int(input("Enter the connection port: "))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    server.bind((host, port))
    server.listen()
except:
    print('Error please try again!')
    sys.exit()


clients= []
bans= []
admins= []
nicknames= []
logging = False

def broadcast(msg):
    for (client, nick) in clients: # pylint: disable=unused-variable
        client.send(msg)

def handle(client):
    global logging
    global bans
    while True:
        try:
            message = client.recv(1024)
            if(logging):
                open("logging.txt", "a").write(message.decode('UTF-8') + '\n')

            isAdmin = message.decode('ascii').split(' ')[0].split(':')[0] in admins
            
            if(message.decode('ascii').split(' ')[1]=='/ban'):
                if(isAdmin):
                    person = message.decode('ascii').split(' ')[2]
                    for clt, nick in clients:
                        if(nick==person):
                            bans.append(person)
                            clt.send('BANNED'.encode('ascii'))
                            broadcast(f'{nick} was banned!'.encode('ascii'))              
                            continue
                else:
                    broadcast(message)
            elif(message.decode('ascii').split(' ')[1]=='/unban'):
                if(isAdmin):
                    person = message.decode('ascii').split(' ')[2]
                    bans.remove(person)
                    broadcast(f'{nick} was unbanned!'.encode('ascii'))              
                    continue
                else:
                    broadcast(message)                                
            elif(message.decode('ascii').split(' ')[1]=='/kick'):
                if(isAdmin):
                    person = message.decode('ascii').split(' ')[2]
                    for clt, nick in clients:
                        if(nick==person):
                            clt.send('KICKED'.encode('ascii'))
                            broadcast(f'{nick} was kicked!'.encode('ascii'))              
                            continue
                else:
                    broadcast(message)
            else:
                broadcast(message)
        except:
            for clt, nick in clients:
                if(clt==client):
                    client, nickname = clt, nick
                    break
            nicknames.remove(nickname)
            clients.remove([client, nickname])
            client.close()
            broadcast(f'\n{nickname} left the chat'.encode('ascii'))
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'Connecting with {str(address)}')
        client.send('NICK'.encode('ascii'))
        try:
            nickname = client.recv(1024).decode('ascii')
        except:
            client.close()
            continue
        if(nickname in bans):
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            client.send('BANNED'.encode('ascii'))
            continue 
        nicknames.append(nickname)
        clients.append([client, nickname])
        print(f'Nickname of the client is: {nickname}!')
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('\nConnected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def write():
    global logging
    while True:
        message = input("")
        if(message=="/help"):
            print("Welcome to Chatting Application!!")
            print("Here are some basic commmands to start with: ")
            print("/help:     Prints the help menu")
            print("/about:    Shows the app information")
            print("/log:      Enables logging")
            print("/promote:  Promote to Admin")
            print("/members:  Shows the list of joined members")
        elif(message=="/about"):
            print('Created by Manan Chawla')
            print('-------------------------')
            print('The program is made using websockets.')
            print('Working: ')
            print('Server listens on a specific port. Whenever a client wants to connect to the server, ')
            print('It sends a tcp request to the server and then server connects the client.')
            print('Additional logging is made possible by file handling')
        elif(message=="/log"):
            logging = not logging
            if(logging):
                print("Now logging the chat")
            else:
                print("Stopped logging the chat")
        elif(message.split(' ')[0]=="/promote"):
            person = message.split(' ')[1]
            if(person in nicknames):
                admins.append(person)
                print(f'{person} is now an admin!')
                broadcast(f'{person} is now an admin!'.encode('ascii'))

            else:
                print('Person not found!')
        elif(message=="/members"):
            for clt, nick in clients: # pylint: disable=unused-variable
                if(nick in nicknames):
                    print(nick)

write_thread = threading.Thread(target=write)
write_thread.start()
print('Initialising Server......')
receive()
