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
        self.currentTime = "" + timeNow.hour + ':' + timeNow.minute
        currentDate = timeNow.date()

        # Unused method to update html
        #subprocess.run(["export", "dynData="+self.currentTime])
        #subprocess.run(["sed", "-i", "s/<h1 class="">.*/<h1 class="">'$(echo $dynData)' <\/h1>/", "/var/www/html/index.html"])

    def display(self) -> None:
        self.update()
        # Updates the HTML
        message = """<h1 class=""> """ + self.currentTime + """ </h1>"""

        return message

