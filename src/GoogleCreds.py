import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/calendar.readonly']


class GoogleCreds():
    def __init__(self):
        self.creds = None
        self.establishCreds()

    def getCreds(self):
        if not self.checkCredValid(self.creds):
            self.creds = self.establishCreds()
        return self.creds

    def checkCredValid(self, creds):
        if not creds or not creds.valid:
            return False
        else:
            return True

    def establishCreds(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                print("1")
                self.creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            print("2")
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
                print("3")
        else:
            print("4")
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
        return self.creds


def main():
    # Calender unit tests
    creds = GoogleCreds()
    creds.getCreds()


if __name__ == '__main__':
    main()
