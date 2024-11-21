import sys
import pygame


class Game:
    """Game object"""
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set screen variable to a resolution of 640, 480
        self.screen = pygame.display.set_mode((640, 480))

        # Set screen title
        pygame.display.set_caption('ninga game')

        # Set clock variable - always limit fps
        self.clock = pygame.time.Clock()

        # Image variable
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0,0,0)) #replace all black pixel with transperency
        self.img_pos = [160, 240] #Image positions
        self.movement = [False, False] #[up, down]


    def run(self):
        while True:
            self.screen.fill((14, 219, 248)) #fill previous rendered screen
            # update image position and scale pos by 5
            self.img_pos[1] += ((self.movement[0] - self.movement[1]) * 5)
            # render img to screen
            self.screen.blit(self.img, self.img_pos)

            # Loop to get input event either from the keyboard or the mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # check if a key is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                # check if a key is released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
            
            # This line update all frame for every loop
            pygame.display.update()
            
            # Maintain 60 fps 
            self.clock.tick(60)

Game().run()