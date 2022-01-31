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
clock = pygame.time.Clock() # Maakt een klok aan

screen = Start.screen() # Start als het ware het scherm op
font = Start.font()
train = Train(screen) # Maakt de trein aan, gedeeltelijk gebaseerd op de waardes van het scherm
slider = Slider(screen, font, 'Snelheid', 0, 0.999, 300, 1620, 100) # Slider(self, screen, font, name, mini, maxi, y_pos, width, height)

Insert.insert
Reset.reset


# MAIN LOOP
while True:
    screen.fill((0, 0, 0)) # Plakt een zwarte laag op het scherm die oude geschreven plaatjes ongedaan maakt

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Als het programma wordt afgesloten door de gebruiker, sluit het ook echt af
            Stop.exit()
    ################################################### Gedeeltelijk gekopieerd
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if slider.button_rect.collidepoint(pos):
                slider.hit = True
        elif event.type == pygame.MOUSEBUTTONUP:
            slider.hit = False

    value = slider.move()
    slider.draw()
    ###################################################

    train.update(value) # Update de waardes van de trein op basis van de snelheid in lichtsnelheden
    train.draw() # Schrijft de trein op het scherm

    clock.tick(60) # Bepaalt het maximale aantal keer per seconde dat de loop uitgevoerd wordt
    pygame.display.flip() # Update het scherm