# IMPORT LIBRARIES
import pygame
from timeit import default_timer as timer


# VARIABLES
RED = (255, 50, 50)


# CLASS
class Clock():
    def __init__(self, screen, font, x, y):
        self.screen = screen
        self.font = font

        self.coordinates = (x, y)

        #self.rectangle = pygame.Rect(100, 300, 100, 100)
        #self.surface = pygame.surface.Surface(self.rectangle)

        self.start = False


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
        self.text = self.font.render(str(round(self.time, 1)), False, RED)
        self.screen.blit(self.text, self.coordinates)