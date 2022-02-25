'''Deze versie bevat tijddilatie en lengtecontractie'''
# IMPORTEREN VAN DE LIBRARIES
import pygame


# IMPORTEREN VAN DE ZELFGEMAAKTE BENODIGDHEDEN
from utils.start import Start
from utils.stop import Stop
from utils.train import Train
from utils.slider import Slider
from utils.clock import Clock

# CONSTANTEN
# De status van de simulatie, 0 = Lengtecontractie, 1 = tijddillatatie, 2 = beide
MIN_SIMULATION = 1
MAX_SIMULATION = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
BLUE = (50, 50, 255)

# VARIABELEN DIE NIET GERESET MOETEN WORDEN EN DIE WEL KUNNEN VERANDEREN
SIMULATION = 1
VALUE = 0
PAUSED = False
DECIMALS = False
PERSPECTIVE = "A"

def main(SIMULATION, VALUE, PAUSED, DECIMALS, PERSPECTIVE):  # Een functie die opnieuw geroepen kan worden als de simulatie gereset of gestart moet worden
    # MAKEN VAN STANDAARD VARIABELEN EN OBJECTEN
    general_clock = pygame.time.Clock()  # Maakt een klok aan

    screen = Start.screen()  # Start als het ware het scherm op
    general_font, clock_font = Start.fonts('lcd_font.ttf')
    init_clocks = False


    # Maakt objecten uit de classes Train en Slider
    # Train(self, screen, image_name, font)
    train = Train(screen, 'trein.png', general_font)
    # Slider(self, screen, font, name, min, max, y_pos, width, height)
    slider = Slider(screen, general_font, 'Snelheid', VALUE, 0, 0.999999, 300, 1620, 100)
    # Clock(self, screen, font, general_font, name, x, y, text_width, text_height, border)
    clock = Clock(screen, clock_font, general_font, "clock", 100, 800, 280, 210, 25)
    reference_clock = Clock(screen, clock_font, general_font, "reference_clock", 1540, 800, 280, 210, 25)


    # Maakt de evenement lijst (van ingedrukte) leeg, zodat ingedrukte knoppen geen ongewenste effecten hebben
    pygame.event.clear()


    # MAIN LOOP
    while True:
        # Plakt een zwarte laag op het scherm die oude geschreven plaatjes ongedaan maakt
        screen.fill((0, 0, 0))

        # Gaat voor elk event na wat er moet gebeuren
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Zorgt voor het afsluiten
                Stop.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if slider.surface_rect.collidepoint(mouse_position):
                    slider.click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                slider.click = False

            elif event.type == pygame.KEYDOWN: # Alle evenementen waarbij de knop is ingedrukt
                if event.key == pygame.K_LEFT:
                    VALUE = slider.move_keyboard(-1)
                elif event.key == pygame.K_RIGHT:
                    VALUE = slider.move_keyboard(1)
                elif event.key == pygame.K_DOWN and SIMULATION > MIN_SIMULATION:
                    SIMULATION -= 1
                    main(SIMULATION, VALUE, PAUSED, DECIMALS, PERSPECTIVE)
                elif event.key == pygame.K_UP and SIMULATION < MAX_SIMULATION:
                    SIMULATION += 1
                    main(SIMULATION, VALUE, PAUSED, DECIMALS, PERSPECTIVE)
                elif event.key == pygame.K_r:
                    pygame.font.quit()
                    main(SIMULATION, VALUE, PAUSED, DECIMALS, PERSPECTIVE)
                elif event.key == pygame.K_SPACE:
                    PAUSED = not PAUSED
                elif event.key == pygame.K_d:
                    DECIMALS = not DECIMALS
                elif event.key == pygame.K_p:
                    if PERSPECTIVE == "A":
                        PERSPECTIVE = "B"
                        main(SIMULATION, VALUE, PAUSED, DECIMALS, PERSPECTIVE)
                    else:
                        PERSPECTIVE = "A"
                        main(SIMULATION, VALUE, PAUSED, DECIMALS, PERSPECTIVE)
                elif event.key == pygame.K_ESCAPE:
                    Stop.exit()



        VALUE = slider.move()
        gamma_factor = slider.gamma()
        slider.draw(DECIMALS)

        if SIMULATION == 1 or SIMULATION == 3:
            # Update de waardes van de trein op basis van de snelheid in lichtsnelheden
            train.update(VALUE, gamma_factor)
            train.draw()  # Schrijft de trein op het scherm
        if SIMULATION == 2 or SIMULATION == 3:
            if PERSPECTIVE == "A":
                if not PAUSED or not init_clocks:
                    init_clocks = True
                    delta_time = clock.update()
                    reference_clock.reference_update(delta_time, gamma_factor)
                clock.draw(PAUSED, PERSPECTIVE)
                reference_clock.draw(PAUSED, PERSPECTIVE)
                screen.blit(general_font[6].render(str(SIMULATION) + " " + PERSPECTIVE, False, BLUE), (70,130))
            else:
                if not PAUSED or not init_clocks:
                    init_clocks = True
                    delta_time = reference_clock.update()
                    clock.reference_update(delta_time, gamma_factor)
                clock.draw(PAUSED, PERSPECTIVE)
                reference_clock.draw(PAUSED, PERSPECTIVE)
                screen.blit(general_font[6].render(str(SIMULATION) + " " + PERSPECTIVE, False, RED), (70,130))

        # Bepaalt het maximale aantal keer per seconde dat de loop uitgevoerd wordt
        general_clock.tick(60)
        pygame.display.flip()  # Update het scherm

main(SIMULATION, VALUE, PAUSED, DECIMALS, PERSPECTIVE)