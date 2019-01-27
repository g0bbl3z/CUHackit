

import sys, pygame, winsound, time
pygame.init()

size = width, height = 800, 500
handheight = 50
black = [0, 0 ,0]

handSprite = pygame.image.load("resources/hand_sprie.png")
spriteRect = handSprite.get_rect()
screen = pygame.display.set_mode(size)

cMajorFile = pygame.mixer.Sound("resources/cMajor.mp3")
aMajorFile = pygame.mixer.Sound("resources/aMajor.mp3")
gMajorFile = pygame.mixer.Sound("resources/gMajor.mp3")


while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP < 500:
            #         handheight += 5
            #     if event.key == pygame.K_DOWN and handheight > 5:
            #         handheight += -5
            #     if event.key == pygame.K_ESCAPE:
            #             sys.exit()

        # if handheight < 170:
        #     # cMajorFile.stop()
        #     cMajorFile.play()
        # elif handheight < 370:
        #     # aMajorFile.stop();
        #     aMajorFile.play();
        # else:
        #     # gMajorFile.stop();
        #     gMajorFile.play();

        # handheight =
        winsound.Beep(300 + handheight, 100)
        screen.fill(black)
        screen.blit(handSprite, (200, 400 - handheight))
        pygame.display.flip()
