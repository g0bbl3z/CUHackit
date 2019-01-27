import Leap
import pygame
import sys


class SampleListener(Leap.Listener):

    def on_init(self, controller):
        print("Initialized")
        pygame.init()
        self.screen = pygame.display.set_mode((0,0))

        self.handSprite = pygame.image.load("../resources/hand_sprite.png")
        self.handHeight = 0

        self.aMajor = pygame.mixer.Sound("resources/aMajor.mp3")
        self.cMajor = pygame.mixer.Sound("resources/cMajor.mp3")
        self.gMajor = pygame.mixer.Sound("resources/gMajor.mp3")

    def on_connect(self, controller):
        print("Connected")

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print("Disconnected")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
            frame = controller.frame()
            # Get hands
            for hand in frame.hands:
                self.handHeight = int(hand.palm_position[1])
                print(self.handHeight)

                #Sound Stuff
                if self.handHeight > 380:
                    pygame.mixer.Sound.play(self.cMajor)
                    pygame.mixer.music.stop()
                elif self.handHeight > 150:
                    pygame.mixer.Sound.play(self.aMajor)
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.Sound.play(self.gMajor)
                    pygame.mixer.music.stop()

                background = [0, 0, 0]
                self.screen.fill(background)
                self.screen.blit(self.handSprite, (200, 400 - self.handHeight))
                pygame.display.flip()

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
