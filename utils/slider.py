import pygame

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
    def __init__(self, name, mini, maxi, x_pos, y_pos, screen, font):
        self.start_value = 0
        self.mini = mini
        self.maxi = maxi
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.screen = screen
        self.font = font

        self.surface = pygame.surface.Surface((100, 50))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction

        self.txt_surf = self.font.render(name, 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(center=(50, 15))

        # Static graphics - slider background #
        self.surface.fill((100, 100, 100))
        pygame.draw.rect(self.surface, GREY, [0, 0, 100, 50], 3)
        pygame.draw.rect(self.surface, ORANGE, [10, 10, 80, 10], 0)
        pygame.draw.rect(self.surface, WHITE, [10, 30, 80, 5], 0)

        self.surface.blit(self.txt_surf, self.txt_rect)  # this surface never changes

        # dynamic graphics - button surface #
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        pygame.draw.circle(self.button_surf, BLACK, (10, 10), 6, 0)
        pygame.draw.circle(self.button_surf, ORANGE, (10, 10), 4, 0)

    def draw(self):
        """
        Combination of static and dynamic graphics in a copy of
        the basic slide surface
        """
        # static
        surf = self.surface.copy()

        # dynamic
        pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*80), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.x_pos, self.y_pos)  # move of button box to correct screen position

        # screen
        self.screen.blit(surf, (self.x_pos, self.y_pos))

    def move(self):
        """
        The dynamic part; reacts to movement of the slider button.
        """
        self.val = (pygame.mouse.get_pos()[0] - self.x_pos - 10) / 80 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi