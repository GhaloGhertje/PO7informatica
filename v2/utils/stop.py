# IMPORT LIBRARIES
import sys, pygame


# CLASS
class Stop():
    def exit():  # Stopt alle processen die zich afspelen als de simulatie actief is
        print('exit')
        pygame.event.clear()
        pygame.font.quit()
        pygame.quit()
        sys.exit()