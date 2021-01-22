from selenium import webdriver
import time
from .util import extract_amount
import os
from .fromownerdotcom import *
from .mycardotcom import *
from .util import crawler, CrawlerType
import requests

chrome_driver_abs_path = os.path.realpath('driver/chromedriver')
firefox_driver_abs_path = os.path.realpath('driver/geckodriver')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())


def get_page_source(url):
    try:
        if crawler() == CrawlerType.REQUESTS:
            payload = {}
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            content = response.content
            logger.info("Status Code => {status_code}".format(status_code=response.status_code))
            logger.info("Headers => {headers}".format(headers=response.headers))
            logger.info("Body => {body}".format(body=content))
            return content
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--disable-blink-features")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_argument('ignore-certificate-errors')

            browser = webdriver.Chrome(executable_path=chrome_driver_abs_path, chrome_options=chrome_options)
            browser.get(url)
            html = browser.page_source
            time.sleep(2)
            browser.quit()
            return html

    except Exception as e:
        logger.error(e)


def get_advert_list(parser, advert_page):
    cur_page = get_page_source(advert_page)
    return parser.get_adverts(cur_page)


def get_adverts_by_url(parser, advert_url, page_count):
    main_page_source = get_page_source(advert_url)

    all_adverts = parser.get_adverts(main_page_source)
    if page_count == 1:
        return all_adverts

    page_list = parser.get_page_list(main_page_source)
    count = 1
    for page in page_list:
        if page_count == count:
            break
        all_adverts.extend(get_advert_list(parser, parser.base_url + page.link))
        count += 1

    return all_adverts


def calculate_total_amount(adverts):
    total_amount = 0
    for advert in adverts:
        total_amount += extract_amount(advert.price)
    return total_amount
