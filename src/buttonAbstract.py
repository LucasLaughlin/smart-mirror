from abc import ABC

class ButtonSubject(ABC):

    @abstractmethod
    def registerObserver(self, observer -> ButtonObserver) -> None:
        # Add observer to the subscriber list
        pass

    @abstractmethod
    def notifyObserver(self) -> None:
        # Uses _state variable of buttons to take call appropriate functions
        pass

class ButtonObserver(ABC):

    @abstractmethod
    def update(self) -> None:
        # Update recieved
        pass

