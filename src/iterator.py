#from twitter.py import TWTTRApp
import rss.py
from time.py import Time
#from alarm.py import Alarm
#import alarmButtons.py

class Iterator:

    def __init__(self):
        self.modules = ["TWTTRApp", "Alarm", "RSSApp", "Time"]

    def __iter__(self):
        return self

    def __next__(self):
        for m in self.modules:
            #if m == "TWTTRApp":
            #    print("twitter!")
            #if m == "Alarm":
            #    theAlarm = Alarm()
            #    alarmObs = alarmButtons.AlarmObserver(theAlarm)
            #    alarmBut = alarmButtons.AlarmButtons()
            #    alarmBut.registerObserver(alarmObs)
            #    alarmBut.waitForInput()

            if m == "RSSApp":
               rssFeed = rss.RSSApp()
               rssFeed.getData()
               rss.updatePosts()

            if m == "Time":
            #   The constructor calls update(), so may remove call to update()
               concreteTime = Time()
               concreteTime.update()
        return self
