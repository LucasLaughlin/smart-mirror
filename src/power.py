# Import tool to allow for monitor power control

class Power:
    _powerState: int = 0

    def __init__(self):
        # The mirror's display will power on as well as the Pi
        pass

    def toggle(self) -> None:
        # Toggles the state of power to the SmartMirror
        if _powerState:
            _powerState = 0
        else:
            _powerState = 1
