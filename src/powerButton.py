import buttonAbstract.py
import power.py

class PowerObserver(ButtonObserver):
    _power: Power = None

    def __init_(self, powerObj: Power) -> None:
        self._power = powerObj

    def update(self) -> None:
        self._power.toggle()

class PowerButton(ButtonSubject):
    # State of the power button
    _state: int = 0

    _observers: List(ButtonObserver)

    def registerObserver(self, observer: PowerObserver) -> None:
        self._observers.append(observer)

    def notifyObserver(self) -> None:
        for observer in observers:
            observer.update(self)

    # Button hardware code
    def toggleState(self) -> None:
        # The power button is pressed
        _state = 1

    def powerLoop(self) -> None:

        if _state:
            notifyObserver()
            _state = 0
