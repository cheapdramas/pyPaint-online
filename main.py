import pygame
from sys import exit
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
       

last_line = ()


def draw():
    global circles,coords,last_line
    circle = Testrect()
    circle.center=pygame.mouse.get_pos()
    circles.append(circle)
    



    for i in range(len(circles)-1):
        try:
            if not circles[i].colliderect( circles[i+1]):
                
                a = pygame.draw.line(window,(255,255,255),circles[i].center,circles[i+1].center,6)
                last_line = (circles[i].center,circles[i+1].center)
        except:
            pass


def get_opposite_draw(my_coordinates:str):

    opposite_draw = client.send(my_coordinates)
    #((x,y),(x,y))
    opposite_draw = ast.literal_eval(opposite_draw)
    if opposite_draw != ():
        pygame.draw.line(window,(255,255,255),opposite_draw[0],opposite_draw[1],6)


draw_avaible = False



while True:
    print(client.connected)
    try:
        get_opposite_draw(str(last_line))
    except:
        print('i guess service is unavaible')


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
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                circles.clear()
                window.fill((0,0,0))


    pygame.display.flip()


        