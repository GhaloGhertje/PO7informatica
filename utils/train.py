import pygame, os

class Train():
    def __init__(self, screen, image_name):
        self.screen = screen

        self.x_mid_position, self.y_mid_position = self.screen.get_size()
        self.x_mid_position /= 2
        self.y_mid_position /= 2

        self.old_velocity = -1
        
        # CODE VOOR WIT VLAK
        #self.height = 500 # Standaard beginhoogte van de trein
        #self.length = self.reference_length = 1000 # Standaard beginlengte van de trein

        # CODE VOOR PlAATJE
        # Afmeting plaatje = 6775 x 510, 1:5 afmeting = 1355 x 102
        #self.height = 500 # Standaard beginhoogte van de trein
        #self.length = self.reference_length = 1000 # Standaard beginlengte van de trein

        self.original_image = pygame.image.load(os.path.join("utils", "images", image_name)) # os.path.join() zorgt ervoor dat het programma ook op ander besturingssystemen afgespeeld kan worden, omdat paths anders werken op verschillende besturingssystemen
        self.original_image_rectangle = self.original_image.get_rect()
        self.length, self.height = self.original_image_rectangle.size

        self.length /= 4
        self.height /= 4

        self.image = pygame.transform.scale(self.original_image, self.original_image_rectangle.size)

    def update(self, velocity):
        if velocity != self.old_velocity: # Beperkt het aantal keer dat de trein geupdate moet worden als er niets veranderd is
            self.old_velocity = velocity

            print('update train')

            self.gamma_factor = 1/(1-(velocity)**2) # Formule gamma waarde, velocity is in lichtsnelheden
            self.reference_length = self.length/self.gamma_factor
            
            # CODE VOOR WIT VLAK
            self.rectangle = pygame.Rect(self.x_mid_position-(self.reference_length/2), self.y_mid_position-(self.height/2), self.reference_length, self.height)

            # CODE VOOR PLAATJE
            #self.position = (self.x_mid_position-(self.reference_length/2), self.y_mid_position-(self.height/2))
            #self.size = (self.reference_length, self.height)
            #self.reference_image = pygame.transform.smoothscale(self.image, (self.reference_length, self.height))

            self.image = pygame.transform.scale(self.original_image, self.rectangle.size)

    def draw(self):
        print('draw train')

        # CODE VOOR WIT VLAK
        #pygame.draw.rect(self.screen, (255,255,255), self.rect) # Wit rechthoek als trein

        # CODE VOOR PlAATJE
        self.screen.blit(self.image, (self.rectangle.x, self.rectangle.y)) # Plaatje als trein