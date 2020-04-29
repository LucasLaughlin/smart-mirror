import configparser
import requests
import sys
from Applet import Applet

class WeatherApplet(Applet):
    def __init__(self, location):
        # Initializes weather attributes and calls getApiKey
        # to prepare for fetching data
        self.coverage = None
        self.temp = None
        self.feelsLike = None
        self.apiKey = None
        self.getApiKey()
        self.location = location

    def getApiKey(self):
        # API key is stored in file config.ini, so the file is parsed
        # and the key is stored as a class attribute
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.apiKey = config['openweathermap']['api']

    def getData(self):
        # The data is requested from the url with a GET request
        # and subsequently stored in the class attributes
        # coverage, temp, and feelsLike
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(
            self.location, self.apiKey)
        response = requests.get(url)
        rjson = response.json()

        # Parsing the returned json file
        self.coverage = rjson['weather'][0]['description']
        self.temp = rjson['main']['temp']
        self.feelsLike = rjson['main']['feels_like']

        # Outputting the information in console for debugging purposes
        print("Coverage: " + str(self.coverage))
        print("Temperature: " + str(self.temp))
        print("Feels Like: " + str(self.feelsLike))

    def display(self):
        # Fetches data before creating the applet's section of HTML
        # The returned string is concatenated to the main view file,
        # which is index.html
        self.getData()
        html = """<div class="pl-2">
                    <p class=" " name="temperature"> Degrees:"""  + str(self.temp) +"""</p>
                    <p class=" " name="cloudcover"> Coverage:""" + str(self.coverage) + """</p>
                </div>"""
        return html


def main():
    weatherApp = WeatherApplet("Boulder")
    weatherApp.getData()

if __name__ == '__main__':
    main()
