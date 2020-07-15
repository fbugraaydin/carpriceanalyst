from enum import Enum


def extract_amount(amount):
    return float(str(amount.split(" ")[0]).replace('.', ''))


def format_date(date):
    return date.strftime("%d/%m")


def format_time(time):
    return time.strftime("%Y-%m-%d %H:%M")


class CrawlerType(Enum):
    SELENIUM = 1,
    REQUESTS = 2


def crawler():
    return CrawlerType.REQUESTS
