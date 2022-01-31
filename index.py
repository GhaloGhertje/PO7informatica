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
slider = Slider('', 0, 0.99, 950, 950, screen, font) # Slider(name, mini, maxi, x_pos, y_pos, screen, font)

Insert.insert
Reset.reset


# MAIN LOOP
while True:
    screen.fill((0, 0, 0)) # Plakt een zwarte laag op het scherm die oude geschreven plaatjes ongedaan maakt

    train.update(0.6) # PAS DE WAARDE AAN DAN MERK JE HET EFFECT # Update de waardes van de trein op basis van de snelheid in lichtsnelheden
    train.draw() # Schrijft de trein op het scherm



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

    slider.move()
    slider.draw()
    ###################################################

    clock.tick(60) # Bepaalt het maximale aantal keer per seconde dat de loop uitgevoerd wordt
    pygame.display.flip() # Update het scherm