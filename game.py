import sys
import pygame
from scripts.entities import PhysicsEntity
from scripts.utils import load_img


class Game:
    """Game object"""
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set screen variable to a resolution of 640, 480
        self.screen = pygame.display.set_mode((640, 480))

        self.display = pygame.Surface((320, 240))

        # Set screen title
        pygame.display.set_caption('ninga game')

        # Set clock variable - always limit fps
        self.clock = pygame.time.Clock()
        self.movement = [False, False] #left and right

        self.assets = {
            'player' : load_img('/entities/player.png')
        }
    
        self.player = PhysicsEntity(self, 'player', (50,50), (8,15))


    def run(self):
        """Run game"""
        while True:
            self.display.fill((14, 219, 248)) #fill previous rendered screen
         
            self.player.update((self.movement[0] - self.movement[1], 0))
            self.player.render(self.display)
            # Loop to get input event either from the keyboard or the mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # check if a key is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.movement[0] = True
                    if event.key == pygame.K_LEFT:
                        self.movement[1] = True
                # check if a key is released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.movement[0] = False
                    if event.key == pygame.K_LEFT:
                        self.movement[1] = False
            

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()))
            # This line update all frame for every loop
            pygame.display.update()
            
            # Maintain 60 fps 
            self.clock.tick(60)

Game().run()