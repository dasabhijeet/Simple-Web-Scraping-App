import re
import requests
from bs4 import BeautifulSoup
import pandas

site_url = 'https://unsplash.com/'

response = requests.get(site_url)
soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]

def image_scraper_func():
  for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png|jpeg|webp))$', url) #can use a-z,A-Z,0-9 regex too

# last updated: 15 July 2024
# repo owner: dasabhijeet.com
