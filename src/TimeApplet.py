import datetime
import subprocess


class Time:
    

    def __init__(self):
        self.update()
        self.currentTime = None
        self.currentDate = None

    def update(self):
        # Gets current time and date
        timeNow = datetime.datetime.now()
        self.currentTime = "" + str(timeNow.hour) + ':' + str(timeNow.minute)
        self.currentDate = timeNow.date()

        # Unused method to update html
        #subprocess.run(["export", "dynData="+self.currentTime])
        #subprocess.run(["sed", "-i", "s/<h1 class="">.*/<h1 class="">'$(echo $dynData)' <\/h1>/", "/var/www/html/index.html"])

    def display(self):
        self.update()
        message = """<h1 class=""> """ + str(self.currentTime) + """ </h1>"""

        return message
