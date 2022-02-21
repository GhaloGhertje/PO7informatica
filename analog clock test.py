import pygame, math, sys
from timeit import default_timer as timer

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def analog(time):
    #__init__
    center_pos = (400, 300)
    radius = 200

    #update
    end_pos = (center_pos[0] + math.sin(time)*radius, center_pos[1] + -math.cos(time)*radius)

    #draw
    pygame.draw.line(screen, BLUE, center_pos, end_pos, 3)
    
time = 0

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    analog(time)    
    
    time += 1/60
    
    pygame.display.flip()
    clock.tick(60)