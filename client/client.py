import socket

class Client():
    def __init__(self) -> None:
        
        self.HEADER = 64
        PORT =5555
        self.FORMAT ='utf-8'
        self.DISCONNECT_MESSAGE = '!LEAVE'
        SERVER=socket.gethostbyname(socket.gethostname())
        self.ADDR = (SERVER,PORT)
        self.connected = False
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        

    def connect(self):
        try:
            self.client.connect(self.ADDR)
            self.connected = True
        except:
            self.connected = False

    def send(self,msg:str):
        if self.connected:
            message = msg.encode(self.FORMAT)
            
            message_len = len(message)
            

            send_len = str(message_len).encode(self.FORMAT)
            send_len+= b' ' *(self.HEADER -len(send_len))
            
            
            self.client.send(send_len)
            self.client.send(message)


            

            coordinates = self.client.recv(2048*10000).decode(self.FORMAT)
            return coordinates
        
   
   


    
   

   
