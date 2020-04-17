import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class CalendarApplet():
    creds = None

    def __init__(self, cred):
        creds = cred

    def storeData(self, cred):
        # Written using example at https://developers.google.com/calendar/quickstart/python

        service = build('calendar', 'v3', credentials=creds)

        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')

        events_result = service.events().list(
                calendarId='primary',
                timeMin=now,
                maxResults=8,
                singleEvents=True,
                orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])
        # Will then display events
