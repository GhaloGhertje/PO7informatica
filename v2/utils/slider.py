# IMPORT LIBRARIES
import pygame


# VARIABLES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)


# CLASS
class Slider():
    def __init__(self, screen, font, name, value, min, max, y_pos, width, height):
        self.screen = screen
        self.font = font

        self.value = value  # Start hoeveelheid
        self.min = min
        self.max = max

        self.width = width
        self.height = height
        self.x_position = (self.screen.get_size()[0] - width)/2
        self.y_position = (y_pos - height)/2

        self.surface = pygame.surface.Surface((self.width, self.height))
        self.click = False  # Als deze aanstaat wordt er met de linker muisknop geklikt op de slider

        self.txt_surf = self.font[4].render(name, 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(
            center=(self.width/2, (self.height/2)-25))

        # STATISCH
        self.surface.fill(WHITE)
        self.surface.blit(self.txt_surf, self.txt_rect)

        self.surface_rect = self.surface.get_rect()
        self.surface_rect.move_ip(self.x_position, self.y_position)


    def draw(self, decimals):  # Plakt de slider op het scherm
        # STATISCH
        self.copy_surface = self.surface.copy()

        # DYNAMISCH
        if decimals:
            self.decimals = 6
        else:
            self.decimals = 3

        # Bepaalt de X positie van het einde van de slider op basis van de waarde die bepaald is door de X positie van de muis
        self.position_slider_x = int(
            (self.value-self.min)/(self.max-self.min)*self.width)

        # Tekent het blauwe gedeelte op basis van de X positie van de slider
        pygame.draw.rect(self.copy_surface, BLUE, [
                         0, 0, self.position_slider_x, self.height])
        
        # Het op het beeld zetten van de slider en de snelheidswaardes
        self.screen.blit(self.copy_surface, (self.x_position, self.y_position))
        self.screen.blit(self.font[0].render(
            "Snelheid: " + str(round(self.value, self.decimals)) + " c", False, WHITE), (100, 50))
        self.value_ms = self.value * 2.99792458*10**8
        self.value_kmh = self.value_ms * 3.6
        self.screen.blit(self.font[0].render(
            "Snelheid: " + str("{:e}".format(int(self.value_ms))) + " m/s", False, WHITE), (800, 50))  # "{:e}.format()" zet de nummers in de wetenschappelijke notatie (bijvoorbeeld: 1,234e+8)
        self.screen.blit(self.font[0].render(
            "Snelheid: " + str("{:e}".format(int(self.value_kmh))) + " km/h", False, WHITE), (1500, 50))


    def move(self):  # Verandert de waarde van de snelheid op basis van de muispositie
        if self.click == True:
            self.value = (pygame.mouse.get_pos()[
                          0] - self.x_position) / self.width * (self.max - self.min) + self.min
            if self.value < self.min:
                self.value = self.min
            if self.value > self.max:
                self.value = self.max

        return self.value


    def move_keyboard(self, direction):  # Verandert de waarde van de snelheid op basis van de pijltjes op het toetsenbord
        if direction == -1:  # Pijltje naar links ingedrukt
            if self.value >= 0 and self.value <= 0.1:
                self.value = self.min
            else:
                self.value = round(self.value-0.051, 1)

        else:  # Pijltje naar rechts ingedrukt
            if self.value >= 0.9:
                self.value = self.max
            else:
                self.value = round(self.value+0.0501, 1)
                if self.value > self.max:
                    self.value = self.max

        return self.value


    def gamma(self):
        # Formule gamma waarde, value is de snelheid in lichtsnelheden
        gamma_factor = 1/((1-(self.value)**2)**0.5)
        return gamma_factor
