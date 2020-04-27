import twitter

class TWTTRApp:
    _twitterAPI: List[String] = twitter.Api(consumer_key='wKLcgF2gPeJUFT5aMgB4UU5p7',
                consumer_secret='g86W2E1K2oqBtRr5U9W5luZOuT3n7avEqqkezvo3ULFgUqedyu',
                access_token_key='632591962-DdnySfMmxLdHHpi8EK42wSMI0k5n2AWDHLwO6NA9',
                access_token_secret='IrKNzqF2fNNrSS2uS6wR6FpEAT1aB6E5armNv8UiclJpW')

    _twttrPosts: List[TWTTRPost] = []

    # Currently handles one TWTTR feed
    def getPosts(self) -> int:

        HNFeed = feedparser(_twitterAPI[0])

        # Checks the format of the XML to make sure that it is valid
        if not HNFeed["bozo"]:
            # Pull out the important info to display
            # Selects top(latest) 10 posts
            for i in range(10):
                post1 = TWTTRPost(HNFeed["item"][0]["title"],
                            HNFeed["item"][1]["description"])
                # Add post to list of posts that will be displayed
                _twttrPosts.append(post1)

        else:
            print("TWTTR app has recieved invalid data")
            # Returns 0 for failed execution
            return 0

        # Returns 1 for successful execution
        return 1


    def getPostList(self) -> List[TWTTRPost]:
        return _twttrPosts


    # Removes posts from display list
    def flushPosts(self) -> None:
        _twttrPosts = []


class TWTTRPost:
    _description: String = ""

    def __init__(self, postTitle: String, postDescription: String) -> None:
        _title = postTitle
        _description = postDescription
