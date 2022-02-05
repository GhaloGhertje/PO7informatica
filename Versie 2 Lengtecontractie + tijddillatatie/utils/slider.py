import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 50)
BLUE = (50, 50, 255)
GREY = (200, 200, 200)

class Slider():
    def __init__(self, screen, font, name, min, max, y_pos, width, height):
        self.screen = screen
        self.font = font

        self.value = 0  # Start hoeveelheid
        self.min = min
        self.max = max

        self.width = width
        self.height = height
        self.x_position = (self.screen.get_size()[0] - width)/2
        self.y_position = (y_pos - height)/2

        self.surface = pygame.surface.Surface((self.width, self.height))
        self.click = False  # Als deze aanstaat wordt er met de linker muisknop geklikt op de slider

        self.txt_surf = self.font.render(name, 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(
            center=(self.width/2, (self.height/2)-25))

        # Statisch
        self.surface.fill(WHITE)
        self.surface.blit(self.txt_surf, self.txt_rect)

        self.surface_rect = self.surface.get_rect()
        self.surface_rect.move_ip(self.x_position, self.y_position)

    def draw(self):  # Plakt de slider op het scherm
        # Statisch
        self.copy_surface = self.surface.copy()

        # Dynamisch
        self.position_slider_x = int(
            (self.value-self.min)/(self.max-self.min)*self.width)

        pygame.draw.rect(self.copy_surface, BLUE, [
                         0, 0, self.position_slider_x, self.height])  # Tekent het blauwe gedeelte

        self.screen.blit(self.copy_surface, (self.x_position, self.y_position))
        self.screen.blit(self.font.render(
            "Snelheid: " + str(round(self.value, 3)) + " c", False, WHITE), (100, 50))
        self.value_ms = self.value * 2.99792458*10**8
        self.value_kmh = self.value_ms * 3.6
        self.screen.blit(self.font.render(
            "Snelheid: " + str(int(round(self.value_ms, 0))) + " m/s", False, WHITE), (800, 50))
        self.screen.blit(self.font.render(
            "Snelheid: " + str(int(round(self.value_kmh, 0))) + " km/h", False, WHITE), (1500, 50))

    def move(self):  # Verandert de waarde van de snelheid op basis van de muispositie
        if self.click == True:
            self.value = (pygame.mouse.get_pos()[
                          0] - self.x_position) / self.width * (self.max - self.min) + self.min
            if self.value < self.min:
                self.value = self.min
            if self.value > self.max:
                self.value = self.max

        return self.value

    def move_keyboard(self, direction):
        if direction == -1:  # Pijltje naar links ingedrukt
            print('left')
            if self.value >= 0 and self.value <= 0.1:
                self.value = self.min
            else:
                self.value = round(self.value-0.051, 1)
           
        else:  # Pijltje naar rechts ingedrukt
            print('right')
            if self.value >= 0.9:
                self.value = self.max
            else:
                self.value = round(self.value+0.0501, 1)
                if self.value > self.max:
                    self.value = self.max

        return self.value

    def gamma(self):
        gamma_factor = 1/(1-(self.value)**0.5) # Formule gamma waarde, value is de snelheid in lichtsnelheden
        return gamma_factor