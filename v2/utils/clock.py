# IMPORT LIBRARIES
from re import A
import pygame, math
from timeit import default_timer as timer


# CONSTANTEN
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
BLUE = (50, 50, 255)


# CLASS
class Clock():
    def __init__(self, screen, font, general_font, name, x, y, text_width, text_height, border):
        self.screen = screen

        self.font = font
        self.general_font = general_font
        self.font_number = 0

        self.name = name
        self.coordinates = (x, y)
        self.text_coordinates = (x, y-2)

        self.text_width = text_width
        self.text_height = text_height
        self.border = border

        # ANALOG CLOCK
        self.radius = text_width/2
        self.center_pos = (self.radius+self.coordinates[0] - self.border, 620)
        self.circle_border = 10

        # TIME & DRAW
        self.start = False
        self.start_draw = False
        self.previous_time = 0.0


    def update(self):
        if not self.start:
            self.start = True
            self.start = self.end = timer()
            self.delta_time = 0.0
            self.time = self.previous_time
        else:
            self.previous = self.end
            self.end = timer()
            self.delta_time = self.end - self.previous
            self.time += self.delta_time*30

        self.calc_radians()

        return self.delta_time


    def reference_update(self, delta_time, gamma_factor):
        if not self.start:
            self.start = True
            self.time = self.previous_time
        else:
            self.time += delta_time / gamma_factor
        
        self.calc_radians()


    def draw(self, paused, perspective):
        # GENERAL
        if paused:
            self.pause_timer()

        if perspective == "A":
            if self.name == "clock":
                text_p = "A"
            else:
                text_p = "B"
            self.screen.blit(self.general_font[6].render(text_p, False, BLUE), (self.coordinates[0] +101, self.coordinates[1] +235))
        else:
            if self.name == "clock":
                text_p = "A"
            else:
                text_p = "B"
            self.screen.blit(self.general_font[6].render(text_p, False, RED), (self.coordinates[0] +101, self.coordinates[1] +235))

        # DIGITAL CLOCK
        self.text = str(round(self.time, 1))
        self.text_render = self.font[self.font_number].render(self.text, False, RED)
        
        if (round(self.time, 2) >= math.pow(10.00, self.font_number)):
            print(str(self.font_number))

            self.text_render = self.general_font[0].render(self.text, False, RED)
            self.text_render = self.font[self.font_number].render(self.text, False, RED)

            self.size_before = self.font[self.font_number].size("10.00")
            self.font_number += 1
            self.size_after = self.font[self.font_number].size("10.00")

            self.width_compensation = -1*self.font_number # -1*self.font_number = de verschuiving naar links van de tekst op basis van de grootte van de tekst in de digitale klok
            self.height_compensation = (self.size_before[1] - self.size_after[1])/2

            #self.text_coordinates = (self.text_coordinates[0] - self.width_compensation, self.text_coordinates[1] + self.height_compensation)
            self.text_coordinates = (self.text_coordinates[0] + self.width_compensation, self.text_coordinates[1] + self.height_compensation)
                        
        self.rect_border = pygame.Rect(self.coordinates[0] -2*self.border, self.coordinates[1], self.text_width +2*self.border, self.text_height +self.border)
        self.rect_background = pygame.Rect(self.coordinates[0] -self.border, self.coordinates[1] +self.border, self.text_width, self.text_height -self.border)

        pygame.draw.rect(self.screen, WHITE, self.rect_border, 25, 10, 10, 10, 10, 10)
        pygame.draw.rect(self.screen, BLACK, self.rect_background)

        self.screen.blit(self.text_render, self.text_coordinates)

        # ANALOG CLOCK
        pygame.draw.circle(self.screen, BLACK, self.center_pos, self.radius+1)
        pygame.draw.circle(self.screen, WHITE, self.center_pos, self.radius+self.circle_border+1, self.circle_border)
        pygame.draw.circle(self.screen, BLUE, self.center_pos, 5)
        pygame.draw.line(self.screen, BLUE, self.center_pos, self.end_pos, 3)


    def calc_radians(self):
        self.radians = (self.time/2)*math.pi  # Elke 12 secondes 1 rondje
        self.end_pos = (self.center_pos[0] + math.sin(self.radians)*self.radius, self.center_pos[1] - math.cos(self.radians)*self.radius)


    def pause_timer(self):
        self.start = False
        self.previous_time = self.time