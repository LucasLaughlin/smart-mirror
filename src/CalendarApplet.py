import datetime
from googleapiclient.discovery import build
from Creds import Creds


class CalendarApplet():

    def __init__(self):
        self.service = None
        self.events = None
        self.messages = None
        self.creds = Creds()
        self.updateService()

    def updateService(self):
        self.service = build(
            'calendar', 'v3', credentials=self.creds.getCreds())

    def getTime(self):
        return datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    def getData(self):
        self.updateService()

        print('Getting the upcoming 10 events')

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
        for event in self.events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            self.messages.append(start + event['summary'])
        return self.events

    def display(self):
        message = """
                <ul class="list-group">
                    <li class="list-group-item"> <h5> Calendar </h5> </li>
                    <li class="list-group-item"> """ + self.messages[0] + """ </li>
                    <li class="list-group-item"> """ + self.messages[1] + """ </li>
                    <li class="list-group-item"> """ + self.messages[2] + """ </li>
                    <li class="list-group-item"> """ + self.messages[3] + """ </li>
                    <li class="list-group-item"> """ + self.messages[4] + """ </li>
                </ul>
                """
        return message

def main():
    # Calender unit tests
    calenderApp = CalendarApplet()
    calenderApp.getData()


if __name__ == '__main__':
    main()
