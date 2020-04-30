from twitter import *
from Applet import Applet
from DataEntry import DataEntry
from ListApplet import ListApplet

class twitterApp(ListApplet):
    def __init__(self):
        super()
        self.title = "Twitter"
        self.entries = list()

    # Get your "home" timeline
    def getData(self):
        t = Twitter(auth=OAuth('Key goes here', 'Key goes here', 'Key goes here', 'Key goes here'))
        if t.statuses.home_timeline()[0]['text'] != None:
            twts = []
            for i in range(5):
                twts.append(DataEntry(t.statuses.home_timeline()[i]['text']))
            self.entries = twts
        else:
            print("Error in pulling twitter data!")
