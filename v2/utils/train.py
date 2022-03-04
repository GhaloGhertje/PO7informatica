# IMPORT LIBRARIES
import pygame
import os


# CLASS
class Train():
    def __init__(self, screen, image_name, font):
        self.screen = screen

        self.x_mid_position, self.y_mid_position = self.screen.get_size()
        self.x_mid_position /= 2
        self.y_mid_position /= 2

        # old_velocity moet gedefinieerd moet worden, maar de waarde mag niet gelijk zijn of groter dan zijn dan 0 aan het begin.
        self.old_velocity = -1

        # os.path.join() zorgt ervoor dat het programma ook op ander besturingssystemen afgespeeld kan worden, omdat paths anders werken op verschillende besturingssystemen
        self.original_image = pygame.image.load(
            os.path.join('v2', 'utils', 'images', image_name))
        self.original_image_rectangle = self.original_image.get_rect()
        self.length, self.height = self.original_image_rectangle.size

        self.length /= 4
        self.height /= 4

        self.image = pygame.transform.scale(
            self.original_image, self.original_image_rectangle.size)
        self.font = font


    def update(self, velocity, gamma_factor):
        if velocity != self.old_velocity:  # Beperkt het aantal keer dat de trein geupdate moet worden als de snelheid niet veranderd is
            self.old_velocity = velocity
            self.percentage = (1/gamma_factor)*100

            self.reference_length = self.length/gamma_factor
            self.rectangle = pygame.Rect((self.x_mid_position-(self.reference_length/2),
                                         self.y_mid_position-(self.height/2)), (self.reference_length,self.height))

            self.image = pygame.transform.scale(
                self.original_image, self.rectangle.size)


    def draw(self, show_percentage):
        # Plaatje als trein
        self.screen.blit(self.image, (self.rectangle.x, self.rectangle.y))

        if show_percentage:
            # int() doet niet hetzelfde als round(), int() haalt de decimalen weg zonder af te ronden
            self.percentage_txt = self.font[4].render(
                str(int(round(self.percentage, 0))) + "%", False, (255, 255, 255))
            self.percentage_rect = self.percentage_txt.get_rect(
                center=(self.x_mid_position, self.y_mid_position-80))
            # Percentage lengte van de trein
            self.screen.blit(self.percentage_txt, self.percentage_rect)
