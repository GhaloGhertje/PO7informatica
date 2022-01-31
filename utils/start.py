import pygame, ctypes

class Start():
    def screen():
        print('start')
        ctypes.windll.user32.SetProcessDPIAware() # Sommige computers werken niet zonder deze functie

        pygame.init() # Start pygame op
        pygame.display.set_caption('Speciale relativiteitstheorie') # Geeft een naam aan de applicatie

        # Display functies
        display_info = pygame.display.Info()
        screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.NOFRAME) # displayInfo.current_w staat voor de width van het scherm die al eerder opgevraagd is. pygame.NOFRAME staat voor windowed borderless
        return screen

    def font():
        print('font')

        pygame.font.init()
        font = pygame.font.SysFont('Arial Black', 18)

        return font