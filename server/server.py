import socket
import threading
import ast
from sys import exit

host= socket.gethostbyname(socket.gethostname())
port=5555
HEADER=64

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((host,port))
except:
    print('error while binding')
coordinates = {
    
}

current_player = 0
def handle_client(conn,addr,player):
    
    
    global coordinates,current_player
    coordinates[player] = '()'
    
   
    print(str(addr) + 'joined!')
    connected = True
    
    while connected:
        
        msg_len = conn.recv(HEADER).decode('utf-8')

        

        if msg_len:
            msg_len = int(msg_len)



            message=conn.recv(msg_len).decode('utf-8')
            

            if message == '!LEAVE':
                connected = False
                
            else:
                try:

                    coordinates[player] = message
                    reply = str([coordinates[i] for i in coordinates.keys() if i != player])
                    # if player == 0:
                    #     coordinates[player]=message
                    #     reply = coordinates[1]

                    # if player == 1:
                    #     coordinates[player] = message
                    #     reply = coordinates[0]
                except:
                    reply = '[]'

            print(reply)
            conn.sendall(reply.encode('utf-8'))


    conn.close()
    coordinates.pop(player)
    current_player -= 1
    print(str(addr)+' disconnected')

    
   


def start():
    global current_player
    s.listen()

    while True:
        
        conn,addr = s.accept()
        thread= threading.Thread(target=handle_client,args=(conn,addr,current_player))
        thread.start()
        current_player += 1




print('starting server.../...')
start()
