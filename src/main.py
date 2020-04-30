from AlarmApplet import AlarmApplet
# from WhiteNoise import WhiteNoiseApplet
from generateHTML import GenerateHTML
import time
from keyboardHelper import KeyboardHelper

def main():
    # This statement triggers a KEYDOWN event when a key is pressed
    concreteAlarm = AlarmApplet()
    # noisemaker = WhiteNoiseApplet()
    keyHelp = KeyboardHelper(concreteAlarm)
    viewGenerator = GenerateHTML(concreteAlarm)

    # KeyboardHelper() has the logic for calling alarm
    keyHelp.startListen()

    viewGenerator.generateHTML()


if __name__ == '__main__':
    main()
