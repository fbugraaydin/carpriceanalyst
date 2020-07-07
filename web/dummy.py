import requests
from bs4 import BeautifulSoup

url = "https://www.sahibinden.com/toyota-corolla"


class Page:
    def __init__(self, index, link):
        self.index = index
        self.link = link

    def __str__(self):
        return "Page Index : {index}, Link: {link} \n".format(index=self.index, link=self.link)


payload = {}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'
}

html_source = requests.request("GET", url, headers=headers, data=payload)

soup = BeautifulSoup(html_source.content, 'html.parser')
nav_items = soup.find("ul", {"class": "pageNaviButtons"}).find_all("li")
parsed_pages = []
for item in nav_items:
    if item.find("a") is not None:
        index = item.find("a").text
        link = "" if item.find("a")['href'] is None else item.find("a")['href']
        parsed_pages.append(Page(index, link))

for p in parsed_pages:
    print(p)
