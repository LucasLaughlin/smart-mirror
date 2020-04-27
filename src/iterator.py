#from twitter.py import TWTTRApp

class Iterator:

    def __init__(self):
        self.modules = ["TWTTRApp"]

    def __iter__(self):
        return self

    def __next__(self):
        for m in self.modules:
            #if m == "TWTTRApp":
            #    print("twitter!")
            
        return self
