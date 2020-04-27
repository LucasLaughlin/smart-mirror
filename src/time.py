import datetime
import subprocess

class Time:
    currentTime: str = ""
    currentDate: str = ""

    def __init__(self) -> None:
        self.update()

    def update(self) -> None:
        # Gets current time and date
        timeNow = datetime.datetime.now()
        currentTime = "" + timeNow.hour + timeNow.minute
        currentDate = timeNow.date()

        # Updates the HTML
        subprocess.run(["export", "dynData="self.currentTime])
        subprocess.run(["sed", "-i", "s/<h1 class="">.*/<h1 class="">'$(echo $dynData)' <\/h1>/", "/var/www/html/index.html"])


