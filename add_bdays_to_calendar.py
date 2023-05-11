import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

path_to_bdays = 'friend_info.json'


with open(path_to_bdays, 'r', encoding='utf-8') as f:
    birthdays = json.load(f)
    
# Authenticate with the Google Calendar API
with open('token.json') as f:
    data = json.load(f)

creds = Credentials.from_authorized_user_info(data)

# Create a service object for interacting with the API
service = build('calendar', 'v3', credentials=creds)
# Loop through each birthday in the list and create a new event on your calendar
for bday in birthdays:
    if bday['bdate'] == "29-02":
        bday['bdate'] = "28-02"
        bday['name'] = f"REAL DATE - 29-02 {bday['name']}"
    bdate = datetime.strptime(bday['bdate'], '%d-%m')
    start = datetime(datetime.now().year, bdate.month, bdate.day, 12, 0, 0).isoformat()
    end = (datetime(datetime.now().year, bdate.month, bdate.day, 12, 0, 0) + timedelta(hours=1)).isoformat()

    event = {
        'summary': f"{bday['name']}'s Birthday",
        'start': {
            'dateTime': start,
            'timeZone': 'Europe/Riga',
        },
        'end': {
            'dateTime': end,
            'timeZone': 'Europe/Riga',
        },
        'recurrence': [
            f'RRULE:FREQ=YEARLY;UNTIL=21001231'
        ],
        'reminders': {
            'useDefault': True,
        },
    }
    #print(f"Event created: {event.get('summary')} {event.get('start')}")
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event created: {event.get('htmlLink')}")