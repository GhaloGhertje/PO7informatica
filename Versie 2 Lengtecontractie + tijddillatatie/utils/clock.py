import pygame
from timeit import default_timer as timer

RED = (255, 50, 50)

class Clock():
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

        self.rectangle = pygame.Rect(100, 300, 100, 100)
        #self.surface = pygame.surface.Surface(self.rectangle)

        self.start = False

    def update(self):
        if not self.start:
            self.start = True
            self.start = timer()
            self.time = 0
        else:
            self.end = timer()
            self.time = self.end - self.start

    def draw(self):
        self.text = self.font.render("T: " + str(round(self.time, 1)), False, RED)
        self.screen.blit(self.text, self.rectangle)