import pygame

class Train():
    def __init__(self, screen):
        print('trijntje oosterhuis')
        self.screen = screen
        self.height = 500 # Standaard beginhoogte van de trein
        self.length = self.reference_length = 1000 # Standaard beginlengte van de trein
        self.old_velocity = 0
        
        self.x_mid_position, self.y_mid_position = self.screen.get_size()
        self.x_mid_position /= 2
        self.y_mid_position /= 2

    def update(self, velocity):
        if velocity != self.old_velocity: #Beperkt het aantal keer dat de trein geupdate moet worden als er niets veranderd is
            self.old_velocity = velocity

            print('update train')
            
            self.gamma_factor = 1/(1-(velocity)**2) # Formule gamma waarde, velocity is in lichtsnelheden
            self.reference_length = self.length/self.gamma_factor
            self.rect = pygame.Rect(self.x_mid_position-(self.reference_length/2), self.y_mid_position-(self.height/2), self.reference_length, self.height)

    def draw(self):
        print('draw train')

        pygame.draw.rect(self.screen, (255,255,255), self.rect)
        #self.screen.blit()