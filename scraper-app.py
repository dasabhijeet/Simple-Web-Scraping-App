import requests
from bs4 import BeautifulSoup
import re
import json
from src.media_scraper.image_scraper import * #/ directory traversal

# initialize
# page_text = ''


# Set URL and response
# url = 'https://www.lawinsider.in'


#response = requests.get(url)
#soup = BeautifulSoup(response.content, 'html.parser')

#title = soup.title.string

# Find text with <p> tags
# page_text = soup.find('p').getText()

'''
# Loop through all <p> tags
data = '' 
for data in soup.find_all("p"): 
    print(data.get_text())

print("\n\n")
'''

url = 'https://www.lawinsider.in'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# For pagination purpose
url_list = []
# Loop through all href links
for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
    url_list.append(link.get('href'))
    #print(link.get('href'))


# Fetch title and content
def fetch_content(url_name):
    response = requests.get(url_name)
    soup = BeautifulSoup(response.content, 'html.parser')

    dictionary = dict();                                # Create new dictionary

    dictionary['title'] = soup.title.string             # Get website title

    data_out = ' '
    for data in soup.find_all("p"):                     # Get all paragraph tags
        data_out = data_out + data.get_text()           # Append them


    dictionary['content'] = data_out 

    return dictionary              # returns title and content both


# Put title and content of each URL and insert them into JSON file (from pagination part)
filename = 'data.json'

for item in range(20, 30, 1):

    new_dictionary = fetch_content(url_list[item])

    with open(filename, 'r+') as f:
        json.dump(new_dictionary, f)


# media scraper call
def media_takeout(link):
    return image_scraper_func(link)
    


'''
filename = 'data.json'

for item in range(20, 30, 1):

    new_dictionary = fetch_content(url_list[item])

    with open(filename, 'r+') as f:
        dic = json.load(f)
        dic.update(new_dictionary)
        json.dump(dic, f)
'''


# entry = fetch_content('https://www.lawinsider.in/news/rpf-members-eligible-for-compensation-under-employees-compensation-act-despite-armed-force-status-supreme-court')



# Written by: https://github.com/dasabhijeet
# Date: 30 September 2023
# Last updated: 15 July 2024
