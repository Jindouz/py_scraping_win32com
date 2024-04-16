import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/United_States'

# # <a href="/wiki/President_of_the_United_States" title="President of the United States">President</a>

# <tr class="mergedrow"><th scope="row" class="infobox-label">
#     <div style="text-indent:-0.9em;margin-left:1.2em;font-weight:normal;">
#     •&nbsp;<a href="/wiki/President_of_the_United_States" title="President of the United States">President</a> 
# </div></th><td class="infobox-data"><a href="/wiki/Joe_Biden" title="Joe Biden">Joe Biden</a></td></tr>

# <td class="infobox-data"><a href="/wiki/Joe_Biden" title="Joe Biden">Joe Biden</a></td>

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# Get all div elements
divs = soup.find_all('tr')
print(f"Number of divs: {len(divs)}")


# Get all anchor elements
anchors = soup.find_all('a')


# Print href for each anchor
print(f"Found {len(anchors)} anchor tags:")
for anchor in anchors:
    href = anchor.get('href')
    print(href)
