import pygame 
import sys 
movement = [False, False]
count = [0,0]

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_mode((200,400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement[0] = True
                print('left key pressed')
            if event.key == pygame.K_RIGHT:
                movement[1] = True
                print('right key pressed')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                movement[0] = False
                print('left key released')
            if event.key == pygame.K_RIGHT:
                movement[1] = False
                print('right key released')
    count[0] += movement[0] - movement[1]
    print(count)
    pygame.display.update()
    clock.tick(2)