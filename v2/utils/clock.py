# IMPORT LIBRARIES
import pygame
from timeit import default_timer as timer


# VARIABLES
RED = (255, 50, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# CLASS
class Clock():
    def __init__(self, screen, font, x, y, text_width, text_height, border):
        self.screen = screen

        self.font = font
        self.font_number = 0

        self.coordinates = (x, y)

        self.text_width = text_width
        self.text_height = text_height
        self.border = border

        #self.rectangle = pygame.Rect(100, 300, 100, 100)
        #self.surface = pygame.surface.Surface(self.rectangle)

        self.start = False
        self.start_draw = False


    def update(self):
        if not self.start:
            self.start = True
            self.start = self.end = timer()
            self.time = self.delta_time = 0.0
        else:
            self.previous = self.end
            self.end = timer()
            self.time = self.end - self.start
            self.delta_time = self.end - self.previous

        return self.delta_time


    def reference_update(self, delta_time, gamma_factor):
        if not self.start:
            self.start = True
            self.time = 0.0
        else:
            self.time += delta_time / gamma_factor


    def draw(self):
        self.text = str(round(self.time, 1))
        self.text_render = self.font[self.font_number].render(self.text, False, RED)
        #self.text_width, self.text_height = self.font[self.font_number].size(self.text)
        
        if (round(self.time, 2) == 10.00**self.font_number):
            self.font_number += 1
            #print(str(self.text_width) + "w/d" + str(self.text_height))
            
        self.rect_border = pygame.Rect(self.coordinates[0] -2*self.border, self.coordinates[1], self.text_width +2*self.border, self.text_height +self.border)
        self.rect_background = pygame.Rect(self.coordinates[0] -self.border, self.coordinates[1] +self.border, self.text_width, self.text_height -self.border)

        pygame.draw.rect(self.screen, WHITE, self.rect_border)
        pygame.draw.rect(self.screen, BLACK, self.rect_background)

        self.screen.blit(self.text_render, self.coordinates)