from bs4 import BeautifulSoup
import requests

search = input("What do you want to search: ")

params = {"q": search}
r = requests.get("http://google.com/search?", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("div", {"id": "main"})
links = results.findAll("div", {"class": "ZINbbc"})

try:
    for item in links:
        item_text = item.find("a").text
        item_href = item.find("a").attrs["href"]

        if item_text and item_href:
            print("Title:", item_text)
            print("Url:", item_href)
            print('''
            ''')
except:
    pass
