import feedparser

class RSSApp:
    _feedURLs: List[String] = ["https://hnrss.org/show?points=200&comments=20"]
    _rssPosts: List[RSSPost] = []

    # Currently handles one RSS feed
    def getPosts(self) -> int:

        HNFeed = feedparser(_feedURLs[0])

        # Checks the format of the XML to make sure that it is valid
        if not HNFeed["bozo"]:
            # Pull out the important info to display
            # Selects top(latest) 10 posts
            for i in range(10):
                post1 = RSSPost(HNFeed["item"][0]["title"],
                            HNFeed["item"][1]["description"])
                # Add post to list of posts that will be displayed
                _rssPosts.append(post1)

        else:
            print("RSS app has recieved invalid XML")
            # Returns 0 for failed execution
            return 0

        # Returns 1 for successful execution
        return 1


    def getPostList(self) -> List[RSSPost]:
        return _rssPosts


    # Removes posts from display list
    def flushPosts(self) -> None:
        _rssPosts = []


class RSSPost:
    _title: String = ""
    _description: String = ""

    def __init__(self, postTitle: String, postDescription: String) -> None:
        _title = postTitle
        _description = postDescription
