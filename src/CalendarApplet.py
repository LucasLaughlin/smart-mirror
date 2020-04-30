import datetime
from googleapiclient.discovery import build
from Creds import Creds
from Applet import Applet
from DataEntry import DataEntry
from ListApplet import ListApplet


class CalendarApplet(ListApplet):
    def __init__(self):
        self.service = None
        self.events = None
        self.entries = list()
        self.creds = Creds()
        self.title = "Upcoming Events"

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
                start = event['start'].get(
                    'dateTime', event['start'].get('date'))
                print(start, event['summary'])
                self.entries.append(DataEntry(event['summary'], start))


def main():
    # Calender unit tests
    calenderApp = CalendarApplet()
    calenderApp.getData()


if __name__ == '__main__':
    main()
