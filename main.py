
import ast
from client.client import Client
import pygame
from pygame import *
init()



clock = pygame.time.Clock()
window = pygame.display.set_mode((500,500))
circles =[]

client = Client()
client.connect()


class Testrect(pygame.Rect):
    def __init__(self):
       self.width=0.1
       self.height=0.1


class Colors:
    def __init__(self):
        self.colors_rgb = {
            'red': (255,0,0),
            'green':(0,255,0),
            'blue':(0,0,255),
            'white': (255,255,255)
        }

        self.rects = {
            'green': pygame.Rect((20,440),(50,50)),
            'red': pygame.Rect((80,440),(50,50)),
            'blue': pygame.Rect((140,440),(50,50))
        }
        
        self.current_color = self.colors_rgb['white']

        self.markup_rect_color = (255,255,255)
        self.markup_rect = Rect((-60,-60),(60,60))

    def show_color_inventory(self):
        for k,rectangle in self.rects.items():
            pygame.draw.rect(window,self.colors_rgb[k],rectangle)
    
    def get_rect_markup(self,rect_obj:pygame.Rect):
        markup_pos = (rect_obj[0] -5,rect_obj[1]-5)
        return markup_pos




    def reset_all_except(self,color):
        center_everyrect = [(self.rects[i].x,self.rects[i].y) for i in self.rects.keys() if i != color]
        
        list_markups_pos = list(map(self.get_rect_markup,center_everyrect))

        for i in list_markups_pos:
            pygame.draw.rect(window,(0,0,0),(i,(60,60)))


       
palette = Colors()


last_circle = ()
def draw():
    global circles,last_circle
    circle = Testrect()
    circle.center=pygame.mouse.get_pos()
    circles.append(circle)
    
    last_circle = ((circle.x,circle.y),(palette.current_color))



    for i in range(len(circles)-1):
        try:
            if not circles[i].colliderect( circles[i+1]):
              
                a = pygame.draw.line(window,palette.current_color,circles[i].center,circles[i+1].center,6)
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
            
            pygame.draw.line(window,list_coord[i][1],list_coord[i][0],list_coord[i+1][0],6)
     




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
            exit()


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
                palette.markup_rect.center = (-60,-60)
                palette.current_color = palette.colors_rgb['white']
            if event.key == K_1:
               
                palette.reset_all_except('green')
                palette.markup_rect.center = (palette.rects['green'].center)
                palette.current_color = palette.colors_rgb['green']
            if event.key == K_2:
                palette.reset_all_except('red')
                palette.markup_rect.center = (palette.rects['red'].center)
                palette.current_color = palette.colors_rgb['red']

            if event.key == K_3:
                palette.reset_all_except('blue')
                palette.markup_rect.center = (palette.rects['blue'].center)
                palette.current_color = palette.colors_rgb['blue']
                
                
    
   

    pygame.draw.rect(window,palette.markup_rect_color,palette.markup_rect)
    palette.show_color_inventory()
    
    clock.tick(120)
    pygame.display.flip()