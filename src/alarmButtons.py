import buttonAbstract.py
import alarm.py

class AlarmObserver(ButtonObserver):
    _alarm: Alarm = None

    def __init__(self, newAlarm: Alarm):
        self._alarm = newAlarm

    def update(self) -> None:
        self._alarm.toggle()

    def updateEarlier(self) -> None:
        self._alarm.earlier()

    def updateLater(self) -> None:
        self._alarm.later()


class AlarmButtons(ButtonSubject):
    # On/Off state of the alarm
    _state: int = 0
    # State of earlier and later buttons
    _later: int = 0
    _earlier: int = 0

    _observers: List[ButtonObserver]

    def registerObserver(self, observer: AlarmObserver) -> None:
        self._observers.append(observer)

    def notifyToggle(self) -> None:
        for observer in _observers:
            observer.updateToggle(self)

    def notifyEarlier(self) -> None:
        for observer in _observers:
            observer.updateEarlier(self)

    def notifyLater(self) -> None:
        for observer in observers:
            observer.updateLater(self)


    # Button Functions will have extra logic when hardware
    # is introduced
    def toggleButton(self) -> None:
        # The alarm toggle button is pressed
        _state = 1

    def earlierButton(self) -> None:
        # The earlier button is pressed
        _earlier = 1

    def laterButton(self) -> None:
        # The later button is pressed
        _later = 1


    def alarmLoop(self) -> None:
        # Checks the status of each button
        # Alerts the observer if any buttons have been pressed
        if _state:
            notifyToggle()
            _state = 0

        if _earlier:
            notifyEarlier()
            _earlier = 0

        if _later:
            notifyLater()
            _later = 0

