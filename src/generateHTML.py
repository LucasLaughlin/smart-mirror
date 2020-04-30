import webbrowser
from GmailApplet import GmailApplet
from rss import RSSApplet
from CalendarApplet import CalendarApplet
from WeatherApplet import WeatherApplet
from ClockApplet import ClockApplet
from AlarmApplet import AlarmApplet
from api_twitter import twitterApp


class GenerateHTML():

    def __init__(self, concAlarm=CalendarApplet()):
        self.f = open('index.html', 'w') #/var/www/index/
        self.gmail = GmailApplet()
        self.calendar1 = concAlarm
        self.rss = RSSApplet()
        self.weather = WeatherApplet("Boulder")
        self.clock = ClockApplet()
        self.alarm = AlarmApplet()
        self.twttr = twitterApp()

    def generate(self):
        message = """<!DOCTYPE html>
            <html lang="en-US">
                <head>
                    <meta charset="UTF-8">
                    <title>SmartMirror</title>
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <!-- Latest compiled and minified CSS -->
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
                    <!-- jQuery library -->
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                    <!-- Popper JS -->
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
                	<style>
            		    body {background-color:black; color: white;}
            		    .list-group-item {background-color:black;}
            		    h5 {border-bottom: 5px solid white;}
            	    </style>
                    </head>
                    <body>
                    <div class="container">
                        <div class="row fixed-top">
                            """ + self.calendar1.display() + """
                            <div class="col p-0"> </div>
                            <div class="col m-4">""" + self.clock.display() + self.weather.display() + self.gmail.display() +"""
                            </div>
                        </div>

                       <div class="row fixed-bottom">
                       """ + self.twttr.display() + """
            	        <div class="col p-0"> </div>
                        """ + self.rss.display() + """
                            </div>

                        </div>
                    </div>
                    </body>
                </html>
                """

        self.f.write(message)
        self.f.close()
        webbrowser.open_new_tab('index.html') #/var/www/index/


def main():
    generateView = GenerateHTML()
    generateView.generate()


if __name__ == '__main__':
    main()
