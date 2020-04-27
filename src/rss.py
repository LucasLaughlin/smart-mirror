import feedparser
import subprocess

class RSSPost:
    _title: str = ""
    _description: str = ""

    def __init__(self, postTitle: str, postDescription: str) -> None:
        _title = postTitle
        _description = postDescription


class RSSApp:
    _feedURL: str = "https://hnrss.org/show?points=200&comments=20"
    _rssPosts = []

    # Currently handles one RSS feed
    def getData(self) -> int:

        HNFeed = feedparser(_feedURL)

        # Checks the format of the XML to make sure that it is valid
        if not HNFeed["bozo"]:
            # Pull out the important info to display
            # Selects top(latest) 10 posts
            for index in range(5):
                post1 = RSSPost(HNFeed["item"][index]["title"],
                            HNFeed["item"][index]["description"])
                # Add post to list of posts that will be displayed
                _rssPosts.append(post1)

        else:
            print("RSS app has recieved invalid XML")
            # Returns 0 for failed execution
            return 0

        # Returns 1 for successful execution
        return 1


    def getPostList(self) -> list:
        return _rssPosts


    # Removes posts from display list
    def flushPosts(self) -> None:
        _rssPosts = []


    def updatePosts(self) -> None:
        # Used to select correct element
        '''
        toChange =["<li name='RSSItemOne.*'", "<li name='RSSItemTwo.*'",
                "<li name='RSSItemThree.*'", "<li name='RSSItemFour.*'",
                "<li name='RSSItemFive.*'"]
        '''

        # The html must be replaced with the appropriate data in each list item
        '''
        changed = ['<li name="RSSItemOne" class="list-group-item">',
                '<li name="RSSItemTwo" class="list-group-item">',
                '<li name="RSSItemThree" class="list-group-item">',
                '<li name="RSSItemFour" class="list-group-item">',
                '<li name="RSSItemFive" class="list-group-item">']
        '''

        # Performs a find and replace for each of the five list items in the view
        '''
        for index in range(5):
            subprocess.run(["export", "dynData="+self._rssPosts[index]._title])
            subprocess.run(["sed", "-i", 's/'+toChange[index]+'/'+changed[index]+"'$(echo $dynData)'<\/li>", "/var/www/html/index.html"])
        '''

        subprocess.run(["export", "dynData=This should be changed")
        subprocess.run(["sed", "-i", "s/<li name='RSSItemOne.*'/<li name='RSSItemFive' class='list-group-item'> This has been changed <\/li>", "/var/www/html/index.html"])

