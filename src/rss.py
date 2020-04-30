import feedparser
import subprocess
from Applet import Applet
from ListApplet import ListApplet
from DataEntry import DataEntry


class RSSApplet(ListApplet):
    def __init__(self):
        super()
        # The RSS url. getData could be altered to accept a list of RSS urls (expanded feature set)
        self._feedURL = "https://hnrss.org/show?points=200&comments=20"
        self.title = "RSS Feed"
        self.entries = list()

    # Currently handles one RSS feed
    def getData(self):

        # The xml retrieved from the Hacker News RSS feed is parsed by feedparser into a dictionary
        HNFeed = feedparser.parse(self._feedURL)

        # Checks the format of the XML to make sure that it is valid
        if not HNFeed["bozo"]:
            # Pull out the important info to display
            # Selects top(latest) 5 posts that fit query criteria
            for index in range(5):
                post1 = HNFeed['entries'][index]['title']

                # Add post to list of posts that will be displayed
                self.entries.append(DataEntry(post1))
        else:
            print("RSS app has recieved invalid XML")
