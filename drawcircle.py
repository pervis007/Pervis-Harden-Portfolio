import pygame

colors = {"white":(255,255,255),
          "blue":(0,0,255),
          "green":(0,255,0),
          "red":(255,0,0)}
(width, height) = (300,300)

def setup():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Harden Circles")
    pygame.display.update()

def drawCircle(c):
    pygame.draw.circle(screen,
                       colors[c.color],
                       (c.coords.x, c.coords.y),
                       c.radius,
                       not c.filled)
    
    