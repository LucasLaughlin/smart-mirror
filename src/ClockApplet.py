import datetime
import subprocess

class ClockApplet:
    def __init__(self):
        self.curMin = None
        self.curHour = None
        self.curDay = None
        self.curMonth = None
        self.curYear = None
        
    def getData(self) -> None:
        # Gets current time and date
        timeNow = datetime.datetime.now()
        self.curHour = timeNow.hour
        self.curMin = timeNow.minute
        today = datetime.datetime.today()
        self.curDay = today.day
        self.curMonth = today.month
        self.curYear = today.year
    
    def display(self) -> None:
        self.getData()
        # Updates the HTML
        html = """<div class="row"><h1> """ + str(self.curHour)+ ":"+ str(self.curMin) + """ </h1>
                    <span class="pl-2 pt-1" >""" + str(self.curMonth) + "/" + str(self.curDay) + "/" + str(self.curYear) +""" </span> </div>""" 
        return html

