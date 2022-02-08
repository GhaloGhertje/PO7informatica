'''Deze versie bevat alleen lengtecontractie'''
# IMPORTEREN VAN DE LIBRARIES
import pygame


# IMPORTEREN VAN DE ZELFGEMAAKTE BENODIGDHEDEN
from utils.start import Start
from utils.insert import Insert
from utils.stop import Stop
from utils.reset import Reset
from utils.train import Train
from utils.slider import Slider


# MAKEN VAN STANDAARD VARIABELEN EN OBJECTEN
clock = pygame.time.Clock()  # Maakt een klok aan

screen = Start.screen()  # Start als het ware het scherm op
font = Start.font()

PRESSED0, PRESSED1 = False, False

# Maakt objecten uit de classes Train en Slider
# Maakt de trein aan, gedeeltelijk gebaseerd op de waardes van het scherm
train = Train(screen, 'trein.png')
# Slider(self, screen, font, name, min, max, y_pos, width, height)
slider = Slider(screen, font, 'Snelheid', 0, 0.999, 300, 1620, 100)

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
        if event.type == pygame.QUIT:  # Zorgt voor juiste afsluiting
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

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and PRESSED0:
                PRESSED0 = False
            elif event.key == pygame.K_RIGHT and PRESSED1:
                PRESSED1 = False

    value = slider.move()
    slider.draw()

    # Update de waardes van de trein op basis van de snelheid in lichtsnelheden
    train.update(value)
    train.draw()  # Schrijft de trein op het scherm

    # Bepaalt het maximale aantal keer per seconde dat de loop uitgevoerd wordt
    clock.tick(60)
    pygame.display.flip()  # Update het scherm
