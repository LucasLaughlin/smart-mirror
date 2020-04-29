from abc import ABC
from abc import abstractmethod

class Applet(ABC):

    @abstractmethod
    def getData(self) -> None:
        pass

    @abstractmethod
    def display(self) -> str:
        return """<div> </div>"""
