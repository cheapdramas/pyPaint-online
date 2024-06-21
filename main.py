import pygame
from sys import exit

clock = pygame.time.Clock()
window = pygame.display.set_mode((500,500))
circles =[]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        

    circle = pygame.draw.circle(window,(255,255,255),pygame.mouse.get_pos(),0.1)
    circles.append(circle)

    for i in range(len(circles)-1):
        
        try:
            if not circles[i].colliderect( circles[i+1]):
                pygame.draw.line(window,(255,255,255),circles[i].center,circles[i+1].center,6)
        except:
            pass
   
    pygame.display.flip()
    