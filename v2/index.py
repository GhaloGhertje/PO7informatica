'''Deze versie bevat tijddilatie en lengtecontractie'''
# IMPORTEREN VAN DE LIBRARIES
import pygame


# IMPORTEREN VAN DE ZELFGEMAAKTE BENODIGDHEDEN
from utils.start import Start
from utils.insert import Insert
from utils.stop import Stop
from utils.reset import Reset
from utils.train import Train
from utils.slider import Slider
from utils.clock import Clock

# VARIABELEN DIE NIET GERESET MOETEN WORDEN
CURRENT_SIMULATION = 0
VALUE = 0
PAUSED = False
DECIMALS = False

def main(CURRENT_SIMULATION, VALUE, PAUSED, DECIMALS):  # Een functie die opnieuw geroepen kan worden als de simulatie gereset of gestart moet worden
    # MAKEN VAN STANDAARD VARIABELEN EN OBJECTEN
    general_clock = pygame.time.Clock()  # Maakt een klok aan

    screen = Start.screen()  # Start als het ware het scherm op
    general_font, clock_font = Start.fonts('lcd_font.ttf')
    init_clocks = False

    PRESSED0, PRESSED1, PRESSED2, PRESSED3, PRESSED4, PRESSED5, PRESSED6 = False, False, False, False, False, False, False

    # Welke simulatie er nu afgespeeld wordt. 0 = Lengtecontractie, 1 = tijddillatatie
    MIN_SIMULATION = 0
    MAX_SIMULATION = 1

    # Maakt objecten uit de classes Train en Slider
    # Maakt de trein aan, gedeeltelijk gebaseerd op de waardes van het scherm
    train = Train(screen, 'trein.png', general_font)
    # Slider(self, screen, font, name, min, max, y_pos, width, height)
    slider = Slider(screen, general_font, 'Snelheid', VALUE, 0, 0.999999, 300, 1620, 100)
    # Clock(self, screen, font, x, y, text_width, text_height, border)
    clock = Clock(screen, clock_font, 100, 800, 280, 210, 25)
    reference_clock = Clock(screen, clock_font, 1540, 800, 280, 210, 25)

    # Roept de variabelen op uit de classes Insert en Reset
    Insert.insert
    Reset.reset

    # Maakt de evenement lijst leeg, zodat ingedrukte knoppen geen ongewenste effecten hebben
    pygame.event.clear()

    # MAIN LOOP
    while True:
        # Plakt een zwarte laag op het scherm die oude geschreven plaatjes ongedaan maakt
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Zorgt voor het afsluiten
                Stop.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if slider.surface_rect.collidepoint(mouse_position):
                    slider.click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                slider.click = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    PRESSED0 = True
                    VALUE = slider.move_keyboard(-1)
                elif event.key == pygame.K_RIGHT:
                    PRESSED1 = True
                    VALUE = slider.move_keyboard(1)
                elif event.key == pygame.K_DOWN and CURRENT_SIMULATION > MIN_SIMULATION:
                    PRESSED2 = True
                    CURRENT_SIMULATION -= 1
                elif event.key == pygame.K_UP and CURRENT_SIMULATION < MAX_SIMULATION:
                    PRESSED3 = True
                    CURRENT_SIMULATION += 1
                elif event.key == pygame.K_r:
                    PRESSED4 = True
                    main(CURRENT_SIMULATION, VALUE, PAUSED, DECIMALS)
                elif event.key == pygame.K_SPACE:
                    PRESSED5 = True
                    PAUSED = not PAUSED
                elif event.key == pygame.K_d:
                    PRESSED6 = True
                    DECIMALS = not DECIMALS

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and PRESSED0:
                    PRESSED0 = False
                elif event.key == pygame.K_RIGHT and PRESSED1:
                    PRESSED1 = False
                elif event.key == pygame.K_DOWN and PRESSED2:
                    PRESSED2 = False
                elif event.key == pygame.K_UP and PRESSED3:
                    PRESSED3 = False
                elif event.key == pygame.K_r and PRESSED4:
                    PRESSED4 = False
                elif event.key == pygame.K_SPACE and PRESSED5:
                    PRESSED5 = False
                elif event.key == pygame.K_d and PRESSED6:
                    PRESSED6 = False

        VALUE = slider.move()
        gamma_factor = slider.gamma()
        slider.draw(DECIMALS)

        if CURRENT_SIMULATION == 0:
            # Update de waardes van de trein op basis van de snelheid in lichtsnelheden
            train.update(VALUE, gamma_factor)
            train.draw()  # Schrijft de trein op het scherm
        else:            
            if not PAUSED or not init_clocks:
                init_clocks = True
                delta_time = clock.update()
                reference_clock.reference_update(delta_time, gamma_factor)
            clock.draw(PAUSED)
            reference_clock.draw(PAUSED)

        # Bepaalt het maximale aantal keer per seconde dat de loop uitgevoerd wordt
        general_clock.tick(60)
        pygame.display.flip()  # Update het scherm

main(CURRENT_SIMULATION, VALUE, PAUSED, DECIMALS)