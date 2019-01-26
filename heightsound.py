

import sys, pygame, winsound
pygame.init()

size = width, height = 800, 500
handheight = 50
black = [0, 0 ,0]

handSprite = pygame.image.load("resources/hand_sprite.png")
spriteRect = handSprite.get_rect()
screen = pygame.display.set_mode(size)

while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP < 1000:
                    handheight += 5
                if event.key == pygame.K_DOWN and handheight > 5:
                    handheight += -5
                if event.key == pygame.K_ESCAPE:
                        sys.exit()

        winsound.Beep(300 + handheight, 100)
        screen.fill(black)
        screen.blit(handSprite, (200, 400 - handheight))
        pygame.display.flip()