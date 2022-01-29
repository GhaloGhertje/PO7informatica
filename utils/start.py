import pygame, ctypes

class Start():
    def __init__():
        start = print('start')

        pygame.init() # Start pygame op
        pygame.display.set_caption('Speciale relativiteitstheorie') # Geeft een naam aan de applicatie

        # Display functies
        displayInfo = pygame.display.Info()
        ctypes.windll.user32.SetProcessDPIAware() # Sommige computers werken niet zonder deze functie
        global screen
        screen = pygame.display.set_mode((displayInfo.current_w, displayInfo.current_h), pygame.NOFRAME) # displayInfo.current_w staat voor de width van het scherm die al eerder opgevraagd is. pygame.NOFRAME staat voor windowed borderless