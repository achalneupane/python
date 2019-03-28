from urllib.request import urlopen
response = urlopen('http://www.unh.edu/halelab/BIOL933/schedule.htm')
html = response.read()
# To get all the links in a page

from bs4 import BeautifulSoup

import requests
r  = requests.get("http://www.unh.edu/halelab/BIOL933/schedule.htm")
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))