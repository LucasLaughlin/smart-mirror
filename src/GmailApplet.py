from googleapiclient.discovery import build
from Creds import Creds
import requests
from Applet import Applet

# If modifying these scopes, delete the file token.pickle.

class GmailApplet(Applet):
    def __init__(self):
        self.messagesUnread = None
        self.service = None
        self.creds = Creds()
        self.updateService()

    def updateService(self):
        self.service = build('gmail', 'v1', credentials=self.creds.getCreds())

    def getData(self):
        self.updateService()
        inbox = self.service.users().labels().get(userId='me',id='INBOX').execute()
        self.messagesUnread = inbox['messagesUnread']
        print("Number of unread messages: " + str(self.messagesUnread))
        return self.messagesUnread

    def display(self) -> str:
        self.getData()
        message = """<div class="pl-2"> <span> Unread Emails: """ + str(self.messagesUnread) + """ <span> </div>"""
        return message


def main():
    # Gmail unit tests
    gmailApp = GmailApplet()
    gmailApp.getData()


if __name__ == '__main__':
    main()
