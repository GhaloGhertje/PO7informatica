# IMPORT LIBRARIES
import pygame
from timeit import default_timer as timer


# VARIABLES
RED = (255, 50, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# CLASS
class Clock():
    def __init__(self, screen, font, x, y):
        self.screen = screen
        self.font = font

        self.coordinates = (x, y)

        #self.rectangle = pygame.Rect(100, 300, 100, 100)
        #self.surface = pygame.surface.Surface(self.rectangle)

        self.start = False
        self.start_draw = False
        self.power = 0


    def update(self):
        if not self.start:
            self.start = True
            self.start = self.end = timer()
            self.time = self.delta_time = 0
        else:
            self.previous = self.end
            self.end = timer()
            self.time = self.end - self.start
            self.delta_time = self.end - self.previous

        return self.delta_time


    def reference_update(self, delta_time, gamma_factor):
        if not self.start:
            self.start = True
            self.time = 0
        else:
            self.time += delta_time / gamma_factor


    def draw(self):
        self.text = str(round(self.time, 1))
        self.text_render = self.font.render(self.text, False, RED)
        self.text_width, self.text_height = self.font.size(self.text)
        
        if (round(self.time, 0) == 10**self.power or not self.start_draw):
            self.start_draw = True

            self.power += 1
            self.rect_border = pygame.Rect(self.coordinates[0] -50, self.coordinates[1], self.text_width +100, self.text_height +50)
            self.rect_background = pygame.Rect(self.coordinates[0] -25, self.coordinates[1] +25, self.text_width +50, self.text_height)

        pygame.draw.rect(self.screen, WHITE, self.rect_border)
        pygame.draw.rect(self.screen, BLACK, self.rect_background)

        self.screen.blit(self.text_render, self.coordinates)