import twitter

class TWTTRApp:
    twitterAPI = twitter.Api(consumer_key='wKLcgF2gPeJUFT5aMgB4UU5p7',
                consumer_secret='g86W2E1K2oqBtRr5U9W5luZOuT3n7avEqqkezvo3ULFgUqedyu',
                access_token_key='nokeys',
                access_token_secret='nokeys')

    _twttrPosts: List[TWTTRPost] = []

    # Currently handles one TWTTR feed
    def getPosts(self) -> int:

        if tweets in twitterAPI:
            timeline = api.GetHomeTimeline(count=5)
            _twttrPosts.append([t.text for t in timeline])

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
