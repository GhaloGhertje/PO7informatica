# IMPORT LIBRARIES
import pygame, ctypes, platform, os


# CLASS
class Start():
    def screen():
        
        if platform.system() == 'Windows':
            ctypes.windll.user32.SetProcessDPIAware() # Sommige windows computers werken niet goed met het programma zonder deze regel. Zonder deze regel kan het beeld vervormd zijn.

        pygame.init() # Start de pygame library op
        pygame.display.set_caption('Speciale relativiteitstheorie') # Geeft een naam aan de applicatie

        # Monitor
        display_info = pygame.display.Info() # Vraagt de monitor specificaties op
        screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME) # displayInfo.current_w staat voor de width van het scherm die al eerder opgevraagd is. pygame.NOFRAME staat voor windowed borderless
        return screen # Geeft het gemaakte object terug naar de plek waar deze functie opgevraagd is


    def fonts():
        # Start de font library op
        pygame.font.init()

        # Stopt de fonts in een variabele
        general_font_0 = pygame.font.SysFont('Arial Black', 18)
        general_font_1 = pygame.font.SysFont('Arial Black', 20)
        general_font_2 = pygame.font.SysFont('Arial Black', 22)
        general_font_3 = pygame.font.SysFont('Arial Black', 24)
        general_font_4 = pygame.font.SysFont('Arial Black', 26)
        general_font_5 = pygame.font.SysFont('Arial Black', 28)
        general_font_6 = pygame.font.SysFont('Arial Black', 30)
        general_font_7 = pygame.font.SysFont('Arial Black', 32)
        general_font_8 = pygame.font.SysFont('Arial Black', 34)

        # Stopt de variabelen in een array
        font = [general_font_0, general_font_1, general_font_2, general_font_3, general_font_4, general_font_5, general_font_6, general_font_7, general_font_8]
        
        # Geeft het gemaakte object terug naar de plek waar deze functie opgevraagd is, hier kunnen de verschillende fonten weer gebruikt worden
        return font


    def clock_fonts(file_name):
        # Start de font library op
        pygame.font.init() 
        
        # Stopt de fonts in een variabele
        clock_font_0 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 180) #general_font
        clock_font_1 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 180) #general_font
        clock_font_2 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 156) #general_font
        clock_font_3 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 132) #general_font
        clock_font_4 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 108) #general_font
        clock_font_5 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 84) #general_font

        # Stopt de variabelen in een array
        clock_font = [clock_font_0, clock_font_1, clock_font_2, clock_font_3, clock_font_4, clock_font_5]

        # Geeft het gemaakte object terug naar de plek waar deze functie opgevraagd is, hier kunnen de verschillende fonten weer gebruikt worden
        return clock_font