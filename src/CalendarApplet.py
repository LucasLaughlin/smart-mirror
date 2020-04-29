import datetime
from googleapiclient.discovery import build
from Creds import Creds
from Applet import Applet


class CalendarApplet(Applet):

    def __init__(self):
        self.service = None
        self.events = None
        self.messages = list()
        self.creds = Creds()

    def updateService(self):
        self.service = build(
            'calendar', 'v3', credentials=self.creds.getCreds())

    def getTime(self):
        return datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    def getData(self):
        self.updateService()

        events_results = self.service.events().list(
            calendarId='primary',
            timeMin=self.getTime(),
            maxResults=8,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        self.events = events_results.get('items', [])

        if not self.events:
            print('No upcoming events found.')
        else:
            for event in self.events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])
                self.messages.append([start, event['summary']])

    def display(self):
        self.getData()
        message = """
                    <div class="col m-4">
                        <ul class="list-group">
                            <li class="list-group-item"> <h5> Calendar Notifications </h5> </li>
                            <li name="CalendarItemOne" class="list-group-item"> """ + self.messages[0][0] + " " + self.messages[0][1] + """ </li>
                            <li name="CalendarItemTwo" class="list-group-item">  """ + self.messages[1][0] + " " + self.messages[1][1] + """  </li>
                            <li name="CalendarItemThree" class="list-group-item"> """ + self.messages[2][0] + " " + self.messages[2][1] + """ </li>
                            <li name="CalendarItemFour" class="list-group-item"> """ + self.messages[3][0] + " " + self.messages[3][1] + """ </li>
                            <li name="CalendarItemFive" class="list-group-item"> """ + self.messages[4][0] + " " + self.messages[4][1] + """ </li>
                        </ul>
                    </div>
                    """
        return message


def main():
    # Calender unit tests
    calenderApp = CalendarApplet()
    calenderApp.getData()


if __name__ == '__main__':
    main()
