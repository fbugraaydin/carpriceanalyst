from selenium import webdriver
import time
from bs4 import BeautifulSoup
from page import Page
from advert import Advert

chrome_driver_abs_path = '/Users/fuatbugra/PycharmProjects/fromowner/driver/chromedriver'
firefox_driver_abs_path = '/Users/fuatbugra/PycharmProjects/fromowner/driver/geckodriver'
advert_url = 'https://www.sahibinden.com/volkswagen-golf-1.4-tsi-comfortline'
base_url = 'https://sahibinden.com'


def get_page_resource(url):
    browser = webdriver.Chrome(executable_path=chrome_driver_abs_path)
    browser.get(url)
    html = browser.page_source
    time.sleep(2)
    browser.close()
    return html


def get_page_list(html_source):
    soup = BeautifulSoup(html_source, 'html.parser')
    nav_items = soup.find("ul", {"class": "pageNaviButtons"}).find_all("li")
    parsed_pages = []
    for item in nav_items:
        if item.find("a") is not None:
            index = item.find("a").text
            link = "" if item.find("a")['href'] is None else item.find("a")['href']
            parsed_pages.append(Page(index, link))
    return parsed_pages


def get_adverts(html_source):
    soup = BeautifulSoup(html_source, 'html.parser')
    adverts = soup.find_all("tr", {"class": "searchResultsItem"})

    parsed_adverts = []
    for advert in adverts:
        advert_columns = advert.find_all("td")
        if advert_columns is not None and len(advert_columns) > 8:
            year = advert_columns[3].text.strip()
            km = advert_columns[4].text.strip()
            price = advert_columns[6].text.strip()
            address = advert_columns[8].text.strip()
            parsed_adverts.append(Advert(year, km, price, address))

    return parsed_adverts


def get_advert_list(advert_page):
    cur_page = get_page_resource(advert_page)
    return get_adverts(cur_page)


main_page_source = get_page_resource(advert_url)
page_list = get_page_list(main_page_source)

lastPage = page_list.__getitem__(len(page_list) - 2)
print("Page count is : {last_page_index}".format(last_page_index=lastPage.index))

all_adverts = []
count = 0
for page in page_list:
    if count > 2:
        break
    all_adverts.extend(get_advert_list(base_url + page.link))
    count += 1


for cur_advert in all_adverts:
    print(cur_advert)

print("All is well")
