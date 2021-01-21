from bs4 import BeautifulSoup
import requests


website = "https://books.toscrape.com"

response = requests.get(website)
soup = BeautifulSoup(response.text, "html.parser")


soup = soup.find("div", {"class": "side_categories"})

soup = soup.find("ul")

soup = soup.find("li")

soup = soup.find_all("a")

categories = []

for a in soup:
    a_content = (a.text).strip()
    categories.append(a_content)

print(categories)
