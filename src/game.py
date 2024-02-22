import pygame
import time as t
import WorldGen

pygame.init()

white = 255,255,255

display = pygame.display.set_mode((1800,1000))
clock = pygame.time.Clock()
background_icon = pygame.image.load(".\\assets\lbackground.jpg") 
#pygame.display.set_icon(background_icon)

class tree:
    def create():





running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Running = False
            quit() 
    #display.fill((0,0,0))
    #display.blit(background_icon, (0,0))
    #pygame.display.flip()
    clock.tick(60)
    pygame.draw.circle(display, white, (20,100), 20)
    pygame.display.update
            