'''Deze file rendert de slider en de tekst die daarboven staat'''
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


# MAKEN VAN STANDAARD VARIABELEN EN OBJECTEN
general_clock = pygame.time.Clock()  # Maakt een klok aan

screen = Start.screen()  # Start als het ware het scherm op
general_font, clock_font = Start.fonts('lcd_font.tff')

PRESSED0, PRESSED1, PRESSED2, PRESSED3 = False, False, False, False
# Welke simulatie er nu afgespeeld wordt. 0 = Lengtecontractie, 1 = tijddillatatie
CURRENT_SIMULATION = 0
MIN_SIMULATION = 0
MAX_SIMULATION = 1

# Maakt objecten uit de classes Train en Slider
# Maakt de trein aan, gedeeltelijk gebaseerd op de waardes van het scherm
train = Train(screen, 'trein.png', general_font)
# Slider(self, screen, font, name, min, max, y_pos, width, height)
slider = Slider(screen, general_font, 'Snelheid', 0, 0.999, 300, 1620, 100)
clock = Clock(screen, clock_font, 100, 980)
reference_clock = Clock(screen, clock_font, 1820, 980)

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
                value = slider.move_keyboard(-1)
            elif event.key == pygame.K_RIGHT:
                PRESSED1 = True
                value = slider.move_keyboard(1)
            elif event.key == pygame.K_DOWN and CURRENT_SIMULATION > MIN_SIMULATION:
                PRESSED0 = True
                CURRENT_SIMULATION -= 1
            elif event.key == pygame.K_UP and CURRENT_SIMULATION < MAX_SIMULATION:
                PRESSED1 = True
                CURRENT_SIMULATION += 1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and PRESSED0:
                PRESSED0 = False
            elif event.key == pygame.K_RIGHT and PRESSED1:
                PRESSED1 = False
            elif event.key == pygame.K_DOWN and PRESSED2:
                PRESSED2 = False
            elif event.key == pygame.K_UP and PRESSED3:
                PRESSED3 = False

    value = slider.move()
    gamma_factor = slider.gamma()
    slider.draw()

    if CURRENT_SIMULATION == 0:
        # Update de waardes van de trein op basis van de snelheid in lichtsnelheden
        train.update(value, gamma_factor)
        train.draw()  # Schrijft de trein op het scherm
    else:
        delta_time = clock.update()
        reference_clock.reference_update(delta_time, gamma_factor)
        clock.draw()
        reference_clock.draw()

    # Bepaalt het maximale aantal keer per seconde dat de loop uitgevoerd wordt
    general_clock.tick(60)
    pygame.display.flip()  # Update het scherm
