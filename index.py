# IMPORTEREN VAN DE LIBRARIES
import pygame


# IMPORTEREN VAN DE ZELFGEMAAKTE BENODIGDHEDEN
from utils.start import Start
from utils.insert import Insert
from utils.stop import Stop
from utils.reset import Reset
from utils.train import Train


# MAKEN VAN STANDAARD VARIABELEN EN OBJECTEN
clock = pygame.time.Clock() # Maakt een klok aan

screen = Start.screen() # Start als het ware het scherm op
train = Train(screen) # Maakt de trein aan, gedeeltelijk gebaseerd op de waardes van het scherm

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

    clock.tick(60) # Bepaalt het maximale aantal keer per seconde dat de loop uitgevoerd wordt
    pygame.display.flip() # Update het scherm