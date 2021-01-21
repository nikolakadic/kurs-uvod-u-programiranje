from bs4 import BeautifulSoup
import requests
import json


urls_to_scrape = open("urls_to_scrape.json", "r")
urls_dict = json.loads(urls_to_scrape.read())

list_of_websites = urls_dict['urls']

responses = []

for webiste in list_of_websites:
    response = requests.get(webiste)
    soup = BeautifulSoup(response.text, 'html.parser')
    responses.append(soup.title.string)

print(responses)