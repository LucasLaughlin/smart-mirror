import datetime
import subprocess

class Time:
    currentTime: String = ""
    currentDate: String = ""

    def __init__(self) -> None:
        self.update()

    def update(self) -> None:
        timeNow = datetime.datetime.now()
        currentTime = "" + timeNow.hour + timeNow.minute
        currentDate = timeNow.date()

        subprocess.run(["export", "dynData", self.currentTime])
        subprocess.run(["sed", 's/<h1 class="">.+/<h1 class=""> $(echo $(dynData)) </h1>/'])


