from twitter import *

class twitterApp:
    def __init__(self):
        self.timeline = ""

    # Get your "home" timeline
    def getPosts(self):
        t = Twitter(auth=OAuth('nokeys', 'nokeys', 'nokeys', 'nokeys'))
        if t.statuses.home_timeline()[0]['text'] is not None:
            twts = []
            for i in range(5):
                twts.append(t.statuses.home_timeline()[i]['text'])
            return twts
        else:
            print("Error in pulling twitter data!")
            return 1


