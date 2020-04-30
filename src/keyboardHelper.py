import pynput
from pynput import keyboard
from AlarmApplet import AlarmApplet
# Made with https://pynput.readthedocs.io/en/latest/keyboard.html

class KeyboardHelper:

    def __init__(self, concAlarm):
        self.alarm = concAlarm

    def on_press(key, letter):
        pass

    def on_release(key, letter):
        #Add your code to stop motor
        if key == keyboard.Key.esc:
            # Stop listener
            # Stop the Robot Code
            return False
        if 'char' in dir(key):     #check if char method exists,
            if key.char == 'a':    #check if it is 'q' key
                print("Alarm On")
                self.alarm.toggleState()

            """
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
            """


    def startListen(self):
        # Collect events until released
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
