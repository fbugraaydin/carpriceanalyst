import logging
from bs4 import BeautifulSoup
from .page import Page
from .advert import Advert

logger = logging.getLogger()


class FromOwnerDotCom:
    base_url = 'https://sahibinden.com'

    @classmethod
    def get_page_list(cls, html_source):
        logger.info('Parsing page list from main page source')
        soup = BeautifulSoup(html_source, 'html.parser')
        nav_items = soup.find("ul", {"class": "pageNaviButtons"}).find_all("li")
        parsed_pages = []
        for item in nav_items:
            if item.find("a") is not None:
                index = item.find("a").text
                link = "" if item.find("a")['href'] is None else item.find("a")['href']
                parsed_pages.append(Page(index, link))
        logger.info('Parsed page list from html source')
        return parsed_pages

    @classmethod
    def get_adverts(cls, html_source):
        logger.info('Parsing adverts from advert page source')
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
        logger.info('Parsed adverts from advert page source')
        return parsed_adverts
