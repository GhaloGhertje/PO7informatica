import pygame, ctypes, platform, os

class Start():
    def screen():
        
        if platform.system() == 'Windows':
            ctypes.windll.user32.SetProcessDPIAware() # Sommige beeldschermen werken niet goed met het programma zonder deze code

        pygame.init() # Start de pygame library op
        pygame.display.set_caption('Speciale relativiteitstheorie') # Geeft een naam aan de applicatie

        # Monitor
        display_info = pygame.display.Info() # Vraagt de monitor specificaties op
        screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.NOFRAME) # displayInfo.current_w staat voor de width van het scherm die al eerder opgevraagd is. pygame.NOFRAME staat voor windowed borderless
        return screen # Geeft het gemaakte object terug naar de plek waar deze functie opgevraagd is

    def fonts(file_name):
        # Start de font library op en maakt een object aan van een systeem font
        pygame.font.init()
        general_font = pygame.font.SysFont('Arial Black', 18)
        
        clock_font_0 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 180) #general_font
        clock_font_1 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 180) #general_font
        clock_font_2 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 160) #general_font
        clock_font_3 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 140) #general_font
        clock_font_4 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 120) #general_font
        clock_font_5 = pygame.font.Font(os.path.join('v2', 'utils', 'fonts', file_name), 100) #general_font

        clock_font = [clock_font_0, clock_font_1, clock_font_2, clock_font_3, clock_font_4, clock_font_5]

        return general_font, clock_font # Geeft het gemaakte object terug naar de plek waar deze functie opgevraagd is