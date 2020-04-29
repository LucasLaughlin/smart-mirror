from AlarmApplet import AlarmApplet
from WhiteNoise import WhiteNoiseApplet
from generateHTML import GenerateHTML
import time
import pygame

def main():
    # https://stackoverflow.com/questions/24352768/python-key-press-and-key-release-listener
    # Pygame has a simpler solution to waiting for user input than originally used
    pygame.init()
    # This statement triggers a KEYDOWN event when a key is pressed
    pygame.key.set_repeat(100, 100)

    concreteAlarm = AlarmApplet()
    noisemaker = WhiteNoiseApplet()

    viewGenerator = GenerateHTML()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                # If key pressed is 'a'
                if event.key == pygame.K_a:
                    # Toggles whether the alarm is active
                    concreteAlarm.toggleState()

                # If key pressed is 's'
                if event.key == pygame.K_s:
                    # Decrements alarm time by fifteen minutes
                    concreteAlarm.earlier()

                # If key pressed is 'd'
                if event.key == pygame.K_d:
                    # Increments alarm time by fiteen minutes
                    concreteAlarm.later()

                # If key pressed is 'w'
                # if event.key == pygame.K_w:
                #    noisemaker.toggleState()

        viewGenerator.generateHTML()


if __name__ == '__main__':
    main()
