import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))

def drawCircle(color, rad, x, y):
    pygame.draw.circle(screen, color, pygame.Vector2(x, y), rad)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    
    drawCircle("red", 40, 30, 30)
    
