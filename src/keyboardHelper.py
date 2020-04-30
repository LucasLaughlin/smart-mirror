import pynput
from pynput import keyboard
from CalendarApplet import CalendarApplet
# Made with https://pynput.readthedocs.io/en/latest/keyboard.html

class KeyboardHelper:

    def __init__(self, concAlarm):
        self.alarm = concAlarm


    def on_press(key, letter):
        try:
            # If key pressed is 'a'
            if letter == 'a':
                # Toggles whether the alarm is active
                print("Alarm On")
                self.alarm.toggleState()

            # If key pressed is 's'
            if letter == 's':
            # Decrements alarm time by fifteen minutes
                self.alarm.earlier()

            # If key pressed is 'd'
            if letter == 'd':
                # Increments alarm time by fiteen minutes
                self.alarm.later()

            # If key pressed is 'w'
            # if letter == 'w':
            #    noisemaker.toggleState(
        except AttributeError:
            # print('Key {0} pressed'.format(key))
            pass


    def on_release(key, thing):
        #Add your code to stop motor
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def startListen(self):
        # Collect events until released
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
