from bs4 import BeautifulSoup
import requests
from io import BytesIO
from PIL import Image


def searchImage():
    search = input("What image do you want ")

    params = {"q": search}
    r = requests.get("https://www.bing.com/images/search?", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            img_obj = requests.get(item.attrs['href']).content
            title = item.attrs['href'].split("/")[-1]
            img = Image.open(BytesIO(img_obj))
            img.save(f"./Images/"+title)
            print(f"./Images/"+title)
        except:
            print("Could not download Image")


searchImage()