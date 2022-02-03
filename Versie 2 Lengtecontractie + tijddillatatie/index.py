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

pressed0, pressed1, pressed2, pressed3 = False, False, False, False
current_simulation = 0 # Welke simulatie er nu afgespeeld wordt. 0 = Lengtecontractie, 1 = tijddillatatie
min_simulation = 0
max_simulation = 1

# Maakt objecten uit de classes Train en Slider
train = Train(screen, 'trein.png', font) # Maakt de trein aan, gedeeltelijk gebaseerd op de waardes van het scherm
slider = Slider(screen, font, 'Snelheid', 0, 0.999, 300, 1620, 100) # Slider(self, screen, font, name, min, max, y_pos, width, height)

# Roept de variabelen op uit de classes Insert en Reset
Insert.insert
Reset.reset

# Maakt de evenement lijst leeg, zodat ingedrukte knoppen die voor de loop worden ingedrukt, geen ongewenste effecten hebben
pygame.event.clear()

# MAIN LOOP
while True:
    screen.fill((0, 0, 0)) # Plakt een zwarte laag op het scherm die oude geschreven plaatjes ongedaan maakt

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Als het programma wordt afgesloten door de gebruiker, sluit het ook echt af
            Stop.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            if slider.surface_rect.collidepoint(mouse_position):
                slider.click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            slider.click = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pressed0 = True
                value = slider.move_keyboard(-1)
            elif event.key == pygame.K_RIGHT:
                pressed1 = True
                value = slider.move_keyboard(1)
            elif event.key == pygame.K_DOWN and current_simulation > min_simulation:
                pressed0 = True
                current_simulation -= 1
            elif event.key == pygame.K_UP and current_simulation < max_simulation:
                pressed1 = True
                current_simulation += 1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and pressed0:
                pressed0 = False
            elif event.key == pygame.K_RIGHT and pressed1:
                pressed1 = False
            elif event.key == pygame.K_DOWN and pressed2:
                pressed2 = False
            elif event.key == pygame.K_UP and pressed3:
                pressed3 = False


    value = slider.move()
    slider.draw()

    if current_simulation == 0:
        train.update(value) # Update de waardes van de trein op basis van de snelheid in lichtsnelheden
        train.draw() # Schrijft de trein op het scherm

    clock.tick(60) # Bepaalt het maximale aantal keer per seconde dat de loop uitgevoerd wordt
    pygame.display.flip() # Update het scherm