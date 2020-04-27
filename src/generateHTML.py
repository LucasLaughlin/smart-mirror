import webbrowser
from GmailApplet import GmailApplet
from rss import RSSApp
from CalendarApplet import CalendarApplet
from WeatherApplet import WeatherApplet
from TimeApplet import Time


class GenerateHTML():

    def __init__(self):
        self.f = open('index.html', 'w') #/var/www/index/
        self.gmail = GmailApplet()
        self.calender = CalendarApplet()
        self.rss = RSSApp()
        self.weather = WeatherApplet("Boulder")
        self.time = Time()

    def generate(self):
        message1 = """<div> blah blah blah </div>"""
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
                            <div class="col m-4"> 
                                <ul class="list-group">
                                    <li class="list-group-item"> <h5> Calendar Notifications </h5> </li>
                                    <li name="CalendarItemOne" class="list-group-item"> First </li>
                                    <li name="CalendarItemTwo" class="list-group-item"> Second </li>
                                    <li name="CalendarItemThree" class="list-group-item"> Third </li>
                                    <li name="CalendarItemFour" class="list-group-item"> Fourth </li>
                                    <li name="CalendarItemFive" class="list-group-item"> Fifth </li>
                                </ul>
                            </div>
                            <div class="col p-0"> </div>
                            <div class="col m-4">""" + self.time.display() + self.weather.display() + self.gmail.display() + """<h3 name="Alarm" class="pt-3"> Alarm:  </h3>
                            </div>
                        </div>
                        
                        <div class="row fixed-bottom">
                            <div class="col m-4"> 
                                <ul class="list-group">
                                    <li class="list-group-item"> <h5> Twitter Highlights </h5> </li>
                                    <li name="TwitterItemOne" class="list-group-item"> RT @reeseynem: #outwest https://t.co/tA4maglajG </li>
                                    <li name="TwitterItemTwo" class="list-group-item"> Why are men more likely to get worse symptoms and die from covid-19? https://t.co/XLOvhxJm6P https://t.co/vni5sHzQt4 </li>
                                    <li name="TwitterItemThree" class="list-group-item"> https://t.co/1j7iyDaO1I </li>
                                    <li name="TwitterItemFour" class="list-group-item"> Never made it as a wise man </li>
                                    <li name="TwitterItemFive" class="list-group-item"> RT @chefjoseandres: And he did the same in Puerto Rico after Maria, and many other times! He is a great guy, friend, leader....tones of car… </li>
                                </ul>
            	        </div>
            	        <div class="col p-0"> </div>
             	        <div class="col m-4 " >""" + self.rss.display()+"""
            	    	</div>
                            </div>
                            <div class="col"> </div>
                            <div class="col"> </div>
                
                        </div>
                    </div>
                    </body>
                </html>"""

        self.f.write(message)
        self.f.close()
        webbrowser.open_new_tab('index.html') #/var/www/index/


def main():
    # Calender unit tests
    generateView = GenerateHTML()
    generateView.generate()


if __name__ == '__main__':
    main()
