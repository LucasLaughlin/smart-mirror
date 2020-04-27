from CalendarApplet import CalendarApplet
from  GmailApplet import GmailApplet

def main():
    gmailApp = GmailApplet()
    calenderApp = CalendarApplet()
    gmailApp.getData()
    calenderApp.getData()

if __name__ == '__main__':
    main()