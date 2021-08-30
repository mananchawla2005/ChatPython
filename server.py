import socket
import sys
import threading
import mysql.connector as msql 

conn = msql.connect(host='localhost',user='root',passwd='',database='chatapp')
if conn.is_connected():
   print("Connection Established")
else:
   print("Connection Errors! Kindly check!!!")
cmd=conn.cursor()
host = input("Enter the ip address of this server: ")
port = int(input("Enter the connection port: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((host, port))
    server.listen()
    cmd.execute(f"INSERT INTO log values(1, DEFAULT, 'SERVER STARTED', 'Started listening on {host}:{port}')")
    conn.commit()   
except :
    print('Error please try again!')
    cmd.execute(f"INSERT INTO log values(2, DEFAULT, 'UNEXPECTED ERROR', 'Could not start the server')")
    conn.commit()
    conn.close()
    sys.exit()

clients= []
bans= []
admins= []
nicknames= []

def broadcast(msg):
    for (client, nick) in clients: # pylint: disable=unused-variable
        client.send(msg)

def handle(client):
    global bans
    while True:
        try:
            message = client.recv(1024)

            isAdmin = message.decode('ascii').split(' ')[0].split(':')[0] in admins
            if(message.decode('ascii').split(' ')[1]=='/ban'):
                if(isAdmin):
                    person = message.decode('ascii').split(' ')[2]
                    for clt, nick in clients:
                        if(nick==person):
                            bans.append(person)
                            cmd.execute(f"INSERT INTO log values(4, DEFAULT, 'ADMIN ACTION', '{person} was banned!')")
                            conn.commit()   
                            clt.send('BANNED'.encode('ascii'))
                            broadcast(f'{nick} was banned!'.encode('ascii'))           
                            continue
                else:
                    broadcast(message) 
                    try:
                        cmd.execute(f"INSERT INTO log values(3, DEFAULT, 'MESSAGE RECIEVED', '{message.decode('ascii').split(':')[0]} said {' '.join(message.decode('ascii').split(' ')[1:])}')")
                        conn.commit()
                    except Exception as e: print(e)
            elif(message.decode('ascii').split(' ')[1]=='/unban'):
                if(isAdmin):
                    person = message.decode('ascii').split(' ')[2]
                    bans.remove(person)
                    cmd.execute(f"INSERT INTO log values(4, DEFAULT, 'ADMIN ACTION', '{person} was unbanned!')")
                    conn.commit()  
                    broadcast(f'{nick} was unbanned!'.encode('ascii'))            
                    continue
                else:
                    broadcast(message)
                    try:
                        cmd.execute(f"INSERT INTO log values(3, DEFAULT, 'MESSAGE RECIEVED', '{message.decode('ascii').split(':')[0]} said {' '.join(message.decode('ascii').split(' ')[1:])}')")
                        conn.commit()
                    except Exception as e: print(e)                              
            elif(message.decode('ascii').split(' ')[1]=='/kick'):
                if(isAdmin):
                    person = message.decode('ascii').split(' ')[2]
                    for clt, nick in clients:
                        if(nick==person):
                            cmd.execute(f"INSERT INTO log values(4, DEFAULT, 'ADMIN ACTION', '{person} was kicked!')")
                            conn.commit() 
                            clt.send('KICKED'.encode('ascii'))
                            broadcast(f'{nick} was kicked!'.encode('ascii'))             
                            continue
                else:
                    broadcast(message)
                    try:
                        cmd.execute(f"INSERT INTO log values(3, DEFAULT, 'MESSAGE RECIEVED', '{message.decode('ascii').split(':')[0]} said {' '.join(message.decode('ascii').split(' ')[1:])}')")
                        conn.commit()
                    except Exception as e: print(e)
            else:
                broadcast(message)
                try:
                    cmd.execute(f"INSERT INTO log values(3, DEFAULT, 'MESSAGE RECIEVED', '{message.decode('ascii').split(':')[0]} said {' '.join(message.decode('ascii').split(' ')[1:])}')")
                    conn.commit()
                except Exception as e: print(e)
        except:
            for clt, nick in clients:
                if(clt==client):
                    client, nickname = clt, nick
                    break
            nicknames.remove(nickname)
            clients.remove([client, nickname])
            client.close()
            broadcast(f'\n{nickname} left the chat'.encode('ascii'))
            cmd.execute(f"INSERT INTO log values(5, DEFAULT, 'USER LEFT THE CHAT', '{nickname} left the chat!')")
            conn.commit()
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'Connecting with {str(address)}')
        client.send('NICK'.encode('ascii'))
        try:
            nickname = client.recv(1024).decode('ascii')
            cmd.execute(f"INSERT INTO log values(6, DEFAULT, 'USER JOINED THE CHAT', '{nickname} joined the chat!')")
            conn.commit()
        except:
            client.close()
            cmd.execute(f"INSERT INTO log values(5, DEFAULT, 'USER LEFT THE CHAT', 'Couldn't make a connection')")
            conn.commit()
            continue
        if(nickname in bans):
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            client.send('BANNED'.encode('ascii'))
            cmd.execute(f"INSERT INTO log values(5, DEFAULT, 'USER LEFT THE CHAT', 'USER IS BANNED')")
            conn.commit()
            continue 
        nicknames.append(nickname)
        clients.append([client, nickname])
        print(f'Nickname of the client is: {nickname}!')
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('\nConnected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def write():
    while True:
        message = input("")
        if(message=="/help"):
            print("Welcome to Chatting Application!!")
            print("Here are some basic commmands to start with: ")
            print("/help:     Prints the help menu")
            print("/about:    Shows the app information")
            print("/promote:  Promote to Admin")
            print("/members:  Shows the list of joined members")
        elif(message=="/about"):
            print('Created by Manan Chawla')
            print('-------------------------')
            print('The program is made using websockets.')
            print('Working: ')
            print('Server listens on a specific port. Whenever a client wants to connect to the server, ')
            print('It sends a tcp request to the server and then server connects the client.')
            print('Additional logging is made possible by use of mysql database.')
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
