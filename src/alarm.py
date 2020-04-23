# Import tool to control volume

class Alarm:
    _alarmHour: int = None
    _alarmMinute: int = None
    _alarmState: int = 0

    def soundAlarm(self) -> None:
        # Triggers the alarm noise
        print("Alarm is activated")

    def toggle(self) -> None:
        # Toggles the state of the alarm
        print("Alarm button has been pressed")
        if _alarmState:
            _alarmState = 0
        else:
            _alarmState = 1

    def earlier(self) -> None:
        # Decrease alarm time by some constant amount
        pass

    def later(self) -> None:
        # Increase alarm time by some constant amount
        pass
