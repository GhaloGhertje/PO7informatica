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


    def draw(self):  # Zet de achtergrond op het scherm
        self.screen.blit(self.original_image, (0,0))


    def update(self, velocity, gamma_factor):
        if velocity != self.old_velocity:  # Beperkt het aantal keer dat de voorgrond geupdate moet worden als de snelheid niet veranderd is
            # Verandert de oude snelheid naar de nieuwe snelheid voor de volgende keer dat de if-statement opgeroepen wordt
            self.old_velocity = velocity

            # Berekent het percentage van de lengte van het object dat wordt bekeken. Dit is mogelijk omdat altijd geldt: gammafactor >= 1
            self.percentage = (1/gamma_factor)*100

            # Berekent de nieuwe lengte en positie (in het midden van het scherm) van het object 
            # Deze wordt gezien door het andere referentie systeem
            self.reference_length = self.length/gamma_factor
            self.rectangle = pygame.Rect(((self.length-self.reference_length)/2,0), (self.reference_length, self.height))

            # Verandert de grootte van het plaatje op het scherm
            self.image = pygame.transform.scale(
                self.original_image, self.rectangle.size)


    def draw_ref(self):  # Zet de vervormde achtergrond/voorgrond op het scherm
        # Zet het veranderde plaatje op het scherm
        self.screen.blit(self.image, (self.rectangle.x, self.rectangle.y))
        
        # Berekent het percentage en berekent de positie van het percentage (in het midden van het scherm)
        self.percentage_txt = self.font[6].render(
            str(int(round(self.percentage, 0))) + '%', False, (255, 255, 255))  # int() doet niet hetzelfde als round(), int() haalt de decimalen weg zonder af te ronden
        self.percentage_rect = self.percentage_txt.get_rect(
            center=(self.length/2, 920))
        
        # Zet de percentage van de lengte van de vervormde achtergrond/voorgrond op het scherm
        self.screen.blit(self.percentage_txt, self.percentage_rect)
