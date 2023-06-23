from bs4 import BeautifulSoup
import requests

URL= 'https://www.vgmusic.com/music/console/sega/32x/'
FILETYPE= '.mid'

def get_soup(url):
    return BeautifulSoup(requests.get(url).content, 'html.parser')

for i in get_soup(URL).find_all('a'):
    mid_link=i.get('href', ' ')
    if mid_link and FILETYPE not in mid_link:
        continue
    else: print(mid_link)
    file_name = mid_link
    with open(file_name, 'wb') as file:
        response = requests.get(URL + mid_link)
        file.write(response.content)