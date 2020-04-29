import feedparser
import subprocess
from Applet import Applet


class RSSPost:
    _title: str = ""

    def __init__(self, postTitle: str) -> None:
        self._title = postTitle


class RSSApplet(Applet):

    def __init__(self):
        # The RSS url. getData could be altered to accept a list of RSS urls (expanded feature set)
        self._feedURL = "https://hnrss.org/show?points=200&comments=20"
        self._rssPosts = []

    # Currently handles one RSS feed
    def getData(self):

        # The xml retrieved from the Hacker News RSS feed is parsed by feedparser into a dictionary
        HNFeed = feedparser.parse(self._feedURL)

        # Checks the format of the XML to make sure that it is valid
        if not HNFeed["bozo"]:
            # Pull out the important info to display
            # Selects top(latest) 5 posts that fit query criteria
            for index in range(5):
                post1 = RSSPost(HNFeed['entries'][index]['title'])

                # Add post to list of posts that will be displayed
                self._rssPosts.append(post1)
        else:
            print("RSS app has recieved invalid XML")

    def display(self):
        # Fetches the RSS data using the getData before building the applet's display html
        self.getData()
        message = """
            <div class="col m-4 " >
                <ul class="list-group">
                    <li class="list-group-item"> <h5> RSS </h5> </li>
                    <li name="RSSItemOne" class="list-group-item"> """ + self._rssPosts[0]._title + """ </li>
                    <li name="RSSItemTwo" class="list-group-item"> """ + self._rssPosts[1]._title + """</li>
                    <li name="RSSItemThree" class="list-group-item"> """ + self._rssPosts[2]._title + """ </li>
                    <li name="RSSItemFour" class="list-group-item"> """ + self._rssPosts[3]._title + """ </li>
                    <li name="RSSItemFive" class="list-group-item"> """ + self._rssPosts[4]._title + """ </li>
                </ul>
            </div> """
        return message
