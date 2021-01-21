from bs4 import BeautifulSoup
import requests


list_of_websites = ['https://example.com/', 'https://facebook.com/', 'https://developers-lab.me']

responses = []

for webiste in list_of_websites:
    response = requests.get(webiste)
    soup = BeautifulSoup(response.text, 'html.parser')
    responses.append(soup.title.string)

print(responses)