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
       

last_circle = ()
def draw():
    global circles,last_circle
    circle = Testrect()
    circle.center=pygame.mouse.get_pos()
    circles.append(circle)
    
    last_circle = circle.center


    for i in range(len(circles)-1):
        try:
            if not circles[i].colliderect( circles[i+1]):
              
                a = pygame.draw.line(window,(255,255,255),circles[i].center,circles[i+1].center,6)
                #last_line = (circles[i].center,circles[i+1].center)
        except:
            pass
    





opp_circles = []
def get_opposite_draw(my_coordinates:str):
    
    whose_coords = {}
   
    opposite_draw = client.send(my_coordinates)
    #(x,y)
    
    opposite_draw = ast.literal_eval(opposite_draw)
    for i in range(len(opposite_draw)):
        whose_coords[i] = ast.literal_eval(opposite_draw[i])


    if len(opp_circles) < len(whose_coords):
        for i in range(len(whose_coords) - len(opp_circles)):
            opp_circles.append([])
    
    for k,v in whose_coords.items():
        if v != ():
            opp_circles[k].append(v)
        if v == ():
            opp_circles[k] = []
    
    for list_coord in opp_circles:
        for i in range(len(list_coord) -1):
            pygame.draw.line(window,(255,255,255),list_coord[i],list_coord[i+1],6)
     




draw_avaible = False



while True:
    
    
  
    if client.connected:
        get_opposite_draw(str(last_circle))


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
                    
                    last_circle = '()'

        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                circles.clear()
                window.fill((0,0,0))

    clock.tick(120)
    pygame.display.flip()