
class Alarm:
    alarmHour: int = None
    alarmMinute: int = None
    alarmOn: int = 0

    def soundAlarm(self) -> None:
        # Triggers the alarm noise
        print("Alarm is activated")

    def update(self) -> None:
        # Toggles the state of the alarm
        print("Alarm button has been pressed")
        if alarmOn:
            alarmOn = 0
        else:
            alarmOn = 1

    def earlier(self) -> None:
        # Decrease alarm time by some constant amount
        pass

    def later(self) -> None:
        # Increase alarm time by some constant amount
        pass
