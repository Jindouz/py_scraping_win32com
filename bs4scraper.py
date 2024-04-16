import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/United_States'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the <a> element for the President's name
president_name_link = soup.find('a', href="/wiki/Joe_Biden")
if president_name_link:
    president_name = president_name_link.text.strip()
else:
    president_name = "Name not found"

speaker_name_link = soup.find('a', href="/wiki/Mike_Johnson_(Louisiana_politician)")
if speaker_name_link:
    speaker_name = speaker_name_link.text.strip()
else:
    speaker_name = "Name not found"


print('==========================')
print("Speaker's Name:", speaker_name)
print("President's Name:", president_name)
print('==========================')

