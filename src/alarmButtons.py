from smart-mirror import buttonAbstract.py
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
        self.notifyToggle()

    def earlierButton(self) -> None:
        # The earlier button is pressed
        self.notifyEarlier()

    def laterButton(self) -> None:
        # The later button is pressed
        self.notifyLater()

    def waitForInput(self) -> None:

        action = input("Waiting for input")
        if action == "a":
            self.toggleButton()
        if action == "d":
            self.laterButton()
        if action == "s":
            self.earlierButton()
