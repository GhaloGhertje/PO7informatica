# IMPORT LIBRARIES
import pygame
import os


# CLASS
class Background():
    def __init__(self, screen, image_name, font):
        self.screen = screen
        # os.path.join() zorgt ervoor dat het programma ook op ander besturingssystemen afgespeeld kan worden, omdat paths anders werken op verschillende besturingssystemen
        self.original_image = pygame.image.load(
            os.path.join('v2', 'utils', 'images', image_name)).convert()
        self.font = font

        # old_velocity moet gedefinieerd moet worden, maar de waarde mag niet gelijk zijn of groter dan zijn dan 0 aan het begin.
        self.old_velocity = -1

        self.length, self.height = self.original_image.get_rect().size

    def draw(self):
        self.screen.blit(self.original_image, (0,0))

    def update(self, velocity, gamma_factor):
        if velocity != self.old_velocity:  # Beperkt het aantal keer dat de voorgrond geupdate moet worden als de snelheid niet veranderd is
            self.old_velocity = velocity
            self.percentage = (1/gamma_factor)*100

            self.reference_length = self.length/gamma_factor
            self.rectangle = pygame.Rect(((self.length-self.reference_length)/2,0), (self.reference_length, self.height))

            self.image = pygame.transform.scale(
                self.original_image, self.rectangle.size)

    def draw_ref(self):
        self.screen.blit(self.image, (self.rectangle.x, self.rectangle.y))

        # int() doet niet hetzelfde als round(), int() haalt de decimalen weg zonder af te ronden
        self.percentage_txt = self.font[4].render(
            str(int(round(self.percentage, 0))) + "%", False, (255, 255, 255))
        self.percentage_rect = self.percentage_txt.get_rect(
            center=(self.length/2, 300))
        # Percentage lengte van de trein
        self.screen.blit(self.percentage_txt, self.percentage_rect)
