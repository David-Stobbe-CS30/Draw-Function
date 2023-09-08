import pygame
import random
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
    colors = ["red", "black", "blue", "yellow", "green"]
    n = random.randint(10, 40)
    for i in range(n):
        drawCircle(colors[random.randint(0, 4)], random.randint(5, 20), random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))

    pygame.display.flip()
    
    
