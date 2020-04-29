import datetime
from ClockApplet import ClockApplet

class AlarmApplet(ClockApplet):
    def __init__(self):
        super()
        self.alarmMin = 0
        self.alarmHour = 12
        self.alarmOn = False
        self.alarmTriggered = False
        
    def checkAlarmTime(self) -> bool:
        return (self.alarmMin==self.curMin) and (self.alarmHour==self.curHour)
    
    def getData(self) -> None:
        super().getData()
        if ( self.alarmOn and self.checkAlarmTime()): 
            self.alarmTriggered = True
        else:
            self.alarmTriggered = False
    
    def display(self) -> None:
        self.getData()
        if self.alarmTriggered: color = 'red'
        else: color = 'white'
        html = """<h3 > """ + str(self.alarmHour)+ ":"+ str(self.alarmMin) + """ </h3>"""
        return html