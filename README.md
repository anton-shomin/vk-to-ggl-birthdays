# VK friends to Google Calendar birthdays importer
Project allows export the list of friends that have visible birth date from VK social network.
List of friends is exported to friend_info.json in format [{"name": "John Doe", "bdate": "05-05"}]
Then list of friends is imported to the google calendar creating recurring yearly events with title "John Doe's Birthday".

## Technologies
- Python 3.* 
- VK API
- Google calendar API


## How to use
1. Complete steps described in "Python quickstart" https://developers.google.com/calendar/api/quickstart/python but for step "Configure the sample" use quickstart.py from this repository.
2. Run *python get_bdays_from_vk.py* file to get friends with birthdays. Only friends that have birthdays displayed will be listed. 
3. Run *python add_bdays_to_calendar.py* file to add birthdays to create new events in calendar recurring yearly starting this year. 