from selenium import webdriver
import time
from bs4 import BeautifulSoup
from .page import Page
from .advert import Advert
from .util import extract_amount
import os
import logging
import traceback

base_url = 'https://sahibinden.com'

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())


def get_page_source(url):
    logger.info('Getting page source from :' + url)
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("user-agent=ChromiumUA")
        browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

        browser.get(url)
        html = browser.page_source
        time.sleep(2)
        browser.quit()
        logger.info('Got page source : ' + url)
        logger.info('Htmlll => ' + html)
        return html
    except Exception as e:
        logger.error(e)
        trace_back = traceback.format_exc()
        message = str(e) + " " + str(trace_back)
        print(message)


def get_page_list(html_source):
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
    logger.info('Parsed adverts from advert page source')

    for p in parsed_adverts:
        print(p)
    return parsed_adverts


def get_advert_list(advert_page):
    cur_page = get_page_source(advert_page)
    return get_adverts(cur_page)


def get_adverts_by_url(advert_url, page_count):
    main_page_source = get_page_source(advert_url)

    all_adverts = get_adverts(main_page_source)
    if page_count == 1:
        return all_adverts

    page_list = get_page_list(main_page_source)
    count = 1
    for page in page_list:
        if page_count == count:
            break
        all_adverts.extend(get_advert_list(base_url + page.link))
        count += 1

    return all_adverts


def calculate_total_amount(adverts):
    total_amount = 0
    for advert in adverts:
        total_amount += extract_amount(advert.price)
    return total_amount
