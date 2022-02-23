# IMPORT LIBRARIES
import sys, pygame, os


# CLASS
class Stop():
    def exit():
        print('exit')
        pygame.event.clear()
        pygame.font.quit()
        pygame.quit()
        sys.exit()