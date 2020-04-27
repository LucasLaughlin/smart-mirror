import configparser
import requests
import sys

class WeatherApplet():
    def __init__(self, location):
        self.coverage = None
        self.temp = None
        self.feelsLike = None
        self.apiKey = None
        self.getApiKey()
        self.location = location 
    
    def getApiKey(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.apiKey = config['openweathermap']['api']
    
    def getData(self):
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(
            self.location, self.apiKey)
        response = requests.get(url)
        rjson = response.json()
        self.coverage = rjson['weather'][0]['description']
        self.temp = rjson['main']['temp']
        self.feelsLike = rjson['main']['feels_like']
        print("Coverage: " + str(self.coverage))
        print("Temperature: " + str(self.temp))
        print("Feels Like: " + str(self.feelsLike))
        
    def get_weather(self, api_key, location):
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(
            location, api_key)
        r = requests.get(url)
        return r.json()


def main():
    weatherApp = WeatherApplet("Boulder")
    weatherApp.getData()

if __name__ == '__main__':
    main()
