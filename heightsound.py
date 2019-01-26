import sys, pygame, winsound

import sys, pygame
pygame.init()

size = width, height = 320, 240
handheight = 300
black = [0, 0 ,0]

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                handheight += 50
            if event.key == pygame.K_DOWN:
                handheight += -50


    winsound.Beep(handheight, 100)

    screen.fill(black)

    pygame.display.flip()
