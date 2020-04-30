import datetime
from ClockApplet import ClockApplet

class AlarmApplet(ClockApplet):
    def __init__(self):
        super()
        self.alarmMin = 0
        self.alarmHour = 12
        self.alarmOn = False
        self.alarmTriggered = False

    def toggleState(self):
        # Switches the state of the alarm, used
        # when the button is pressed
        if self.alarmOn:
            self.alarmOn = 0
            print("Alarm is active")
        if not self.alarmOn:
            self.alarmOn = 1
            print("Alarm is inactive")

    def checkAlarmTime(self) -> bool:
        # Checks whether the time is equal to the alarm time
        return (self.alarmMin==self.curMin) and (self.alarmHour==self.curHour)

    def earlier(self) -> None:
        # Reduces the time of the alarm by fifteen minutes
        theTime = datetime(self.year, self.month, self.day, hour=self.alarmHour, minute=self.alarmMin)
        newTime = theTime - datetime.timedelta(minutes=15)
        self.alarmHour = newTime.datetime.hour
        self.alarmMinute = newTime.datetime.minute

    def later(self) -> None:
        # Increases the alarm time by fifteen minutes
        theTime = datetime(self.year, self.month, self.day, hour=self.alarmHour, minute=self.alarmMin)
        newTime = theTime + datetime.timedelta(minutes=15)
        self.alarmHour = newTime.datetime.hour
        self.alarmMinute = newTime.datetime.minute

    # Override of ClockApplet
    def getData(self) -> None:
        # Uses ClockApplet's getData() to retrieve the time
        super().getData()
        # Checks to see if the alarm state is active and the
        # alarm time is equal to the current time
        if ( self.alarmOn and self.checkAlarmTime()):
            self.alarmTriggered = True
        else:
            self.alarmTriggered = False

    # Override of ClockApplet
    def display(self) -> None:
        self.getData()
        if self.alarmTriggered: color = 'red'
        else: color = 'white'
        html = """<h3 > """ + str(self.alarmHour)+ ":"+ str(self.alarmMin) + """ </h3>"""
        return html
