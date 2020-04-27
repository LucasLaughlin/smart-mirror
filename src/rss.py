import feedparser
import subprocess


class RSSPost:
    _title: str = ""
    _description: str = ""

    def __init__(self, postTitle: str, postDescription: str) -> None:
        _title = postTitle
        _description = postDescription


class RSSApp:

    def __init__(self):
        self._feedURL = "https://hnrss.org/show?points=200&comments=20"
        self._rssPosts = []
    # Currently handles one RSS feed
    def getData(self):

        HNFeed = (self._feedURL)

        # Checks the format of the XML to make sure that it is valid
        if not HNFeed["bozo"]:
            # Pull out the important info to display
            # Selects top(latest) 10 posts
            for index in range(5):
                post1 = RSSPost(HNFeed["item"][index]["title"],
                                HNFeed["item"][index]["description"])
                # Add post to list of posts that will be displayed
                self._rssPosts.append(post1)

        else:
            print("RSS app has recieved invalid XML")
            # Returns 0 for failed execution
            return 0

        # Returns 1 for successful execution
        return 1

    def getPostList(self):
        return self._rssPosts

    # Removes posts from display list

    def flushPosts(self):
        _rssPosts = []

    def display(self):
        self.getData()
        message = """
                <ul class="list-group">
                    <li class="list-group-item"> <h5> RSS </h5> </li>
                    <li class="list-group-item"> """ + self._rssPosts[0]._title + """ </li>
                    <li class="list-group-item"> """ + self._rssPosts[1]._title + """ </li>
                    <li class="list-group-item"> """ + self._rssPosts[2]._title + """ </li>
                    <li class="list-group-item"> """ + self._rssPosts[3]._title + """ </li>
                    <li class="list-group-item"> """ + self._rssPosts[4]._title + """ </li>
                </ul>
                """
        return message
