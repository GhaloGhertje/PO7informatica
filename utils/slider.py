import pygame

################################################### Gedeeltelijk gekopieerd
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 50)
BLUE = (50, 50, 255)
GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
TRANS = (1, 1, 1)

class Slider():
    def __init__(self, screen, font, name, mini, maxi, y_pos, width, height):
        self.screen = screen
        self.font = font
        
        self.value = 0 # Start hoeveelheid
        self.mini = mini
        self.maxi = maxi
        
        self.width = width
        self.height = height
        self.x_position = (self.screen.get_size()[0] - width)/2
        self.y_position = (y_pos - height)/2

        self.surface = pygame.surface.Surface((self.width, self.height))
        self.click = False  # the hit attribute indicates slider movement due to mouse interaction

        self.txt_surf = self.font.render(name, 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(center=(self.width/2, (self.height/2)-25))

        # Statisch
        self.surface.fill(WHITE)
        #pygame.draw.rect(self.surface, GREY, [0, 0, self.width, self.height], 3)
        #pygame.draw.rect(self.surface, ORANGE, [10, 10, 80, 10], 0)
        #pygame.draw.rect(self.surface, WHITE, [10, 30, self.width-70, self.height-70], 0)

        self.surface.blit(self.txt_surf, self.txt_rect)  # this surface never changes

        # Dynamisch
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        pygame.draw.circle(self.button_surf, BLACK, (10, 10), 6, 0)
        pygame.draw.circle(self.button_surf, GREY, (10, 10), 4, 0)

    def draw(self): # Plakt de slider op het scherm
        # Statisch
        surf = self.surface.copy()

        # Dynamisch
        pos = (int((self.value-self.mini)/(self.maxi-self.mini)*self.width), self.height/2)
        #pos = (10+int((self.value-self.mini)/(self.maxi-self.mini)*80), 33)
        #pos = (10+self.x_position+(self.width*(self.value))/2, self.y_position+self.height/2)

        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.x_position, self.y_position)  # move of button box to correct screen position

        pygame.draw.rect(surf, BLUE, [0, 0, pos[0], self.height])

        self.screen.blit(surf, (self.x_position, self.y_position))
        self.screen.blit(self.font.render("Snelheid: " + str(self.value) + " c", False, WHITE), (100,50))
        self.value_ms = self.value * 2.99792458*10**8
        self.value_kmh = self.value_ms * 3.6
        self.screen.blit(self.font.render("Snelheid: " + str(self.value_ms) + " m/s", False, WHITE), (800,50))
        self.screen.blit(self.font.render("Snelheid: " + str(self.value_kmh) + " km/h", False, WHITE), (1500,50))

    def move(self): # Verandert de waarde van de snelheid op basis van de muispositie
        if self.click == True:
            self.value = (pygame.mouse.get_pos()[0] - self.x_position) / self.width * (self.maxi - self.mini) + self.mini
            if self.value < self.mini:
                self.value = self.mini
            if self.value > self.maxi:
                self.value = self.maxi
        
        return self.value
###################################################