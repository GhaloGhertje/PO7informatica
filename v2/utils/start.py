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
        screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.NOFRAME) # displayInfo.current_w staat voor de width van het scherm die al eerder opgevraagd is. pygame.NOFRAME staat voor windowed borderless
        return screen # Geeft het gemaakte object terug naar de plek waar deze functie opgevraagd is


    def fonts():
        # Start de font library op en maakt een object aan van een systeem font
        pygame.font.init()

        general_font_0 = pygame.font.SysFont('Arial Black', 18)
        general_font_1 = pygame.font.SysFont('Arial Black', 20)
        general_font_2 = pygame.font.SysFont('Arial Black', 22)
        general_font_3 = pygame.font.SysFont('Arial Black', 24)
        general_font_4 = pygame.font.SysFont('Arial Black', 26)
        general_font_5 = pygame.font.SysFont('Arial Black', 28)
        general_font_6 = pygame.font.SysFont('Arial Black', 30)

        font = [general_font_0, general_font_1, general_font_2, general_font_3, general_font_4, general_font_5, general_font_6]

        return font # Geeft het gemaakte object terug naar de plek waar deze functie opgevraagd is


    def clock_fonts(file_name):
        # Start de font library op en maakt een object aan van een systeem font
        pygame.font.init() 
        
        clock_font_0 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 180) #general_font
        clock_font_1 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 180) #general_font
        clock_font_2 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 156) #general_font
        clock_font_3 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 132) #general_font
        clock_font_4 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 108) #general_font
        clock_font_5 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 84) #general_font

        clock_font = [clock_font_0, clock_font_1, clock_font_2, clock_font_3, clock_font_4, clock_font_5]

        return clock_font # Geeft het gemaakte object terug naar de plek waar deze functie opgevraagd is