import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/calendar.readonly']

class Creds():
    
    def __init__(self):
        self.creds = None
        self.establishCreds(self.creds)
    
    def getCreds(self):
        if not self.checkCredValid(self.creds):
            self.creds = self.establishCreds(self.creds)
        return self.creds
    
    def checkCredValid(self, creds):
        if not creds or not creds.valid:
            return False
        else:
            return True
    
    def establishCreds(self, creds):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds

