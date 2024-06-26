import pygame
import ast
from client.client import Client
    

    
pygame.init()



clock = pygame.time.Clock()
window = pygame.display.set_mode((500,500))
circles =[]

client = Client()
client.connect()


class Testrect(pygame.Rect):
    def __init__(self):
       self.width=0.1
       self.height=0.1
       

last_line =[]

last_tuple = ()
def draw():
    global circles,last_line,last_tuple
    circle = Testrect()
    circle.center=pygame.mouse.get_pos()
    circles.append(circle)
    
    last_line.append(circle.center)


    for i in range(len(circles)-1):
        try:
            if not circles[i].colliderect( circles[i+1]):
              
                a = pygame.draw.line(window,(255,255,255),circles[i].center,circles[i+1].center,6)
                #last_line = (circles[i].center,circles[i+1].center)
        except:
            pass
    if len(last_line) == 2:
        last_tuple = (last_line[0],last_line[1])
        last_line.clear()



opp_draw =[]
def get_opposite_draw(my_coordinates:str):
    global opp_draw
    opposite_draw = client.send(my_coordinates)
    #((x,y),(x,y))
    
    opposite_draw = ast.literal_eval(opposite_draw)
    print(opposite_draw)
    if opposite_draw != ():
        opp_draw.append(opposite_draw[0])
        opp_draw.append(opposite_draw[1])
        for i in range(len(opp_draw)-1):
            
            pygame.draw.line(window,(255,255,255),opp_draw[i],opp_draw[i+1],6)
    
            
            

draw_avaible = False



while True:
    
    
    
  
   
    get_opposite_draw(str(last_tuple))
    


    if draw_avaible:
        draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if client.connected:
                client.send('!LEAVE')
            pygame.quit()


        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                draw_avaible= True


        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                draw_avaible= False
                circles.clear()
                if client.connected:
                    
                    last_tuple = '()'

        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                circles.clear()
                window.fill((0,0,0))

    clock.tick(120)
    pygame.display.flip()


        