from twitter import *

class twitterApp:
    def __init__(self):
        self.timeline = ""
        self.feed = list()

    # Get your "home" timeline
    def getData(self):
        t = Twitter(auth=OAuth('nokeys', 'nokeys', 'nokeys', 'nokeys'))
        if t.statuses.home_timeline()[0]['text'] is not None:
            twts = []
            for i in range(5):
                twts.append(t.statuses.home_timeline()[i]['text'])
            self.feed = twts
        else:
            print("Error in pulling twitter data!")
            return 1


    def display(self):
        self.getData()
        message = """
            <div class="col m-4">
                <ul class="list-group">
                    <li class="list-group-item"> <h5> Twitter Highlights </h5> </li>
                    <li name="TwitterItemOne" class="list-group-item"> + self.tweets[0]+ </li>
                    <li name="TwitterItemTwo" class="list-group-item"> +self.tweets[1]+</li>
                    <li name="TwitterItemThree" class="list-group-item"> + self.tweets[2] +</li>
                    <li name="TwitterItemFour" class="list-group-item"> + self.tweets[3] +</li>
                    <li name="TwitterItemFive" class="list-group-item"> + self.tweets[4] +</li>
                </ul>
            </div>
        """
        return message
