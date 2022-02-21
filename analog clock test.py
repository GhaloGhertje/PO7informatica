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
    border = 10

    #update
    radians = (time/6)*math.pi  # Elke 12 secondes 1 rondje
    end_pos = (center_pos[0] + math.sin(radians)*radius, center_pos[1] + -math.cos(radians)*radius)

    #draw
    pygame.draw.circle(screen, WHITE, center_pos, radius+border+1, border)
    pygame.draw.circle(screen, BLUE, center_pos, 5)
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