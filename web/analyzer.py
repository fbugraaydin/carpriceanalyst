from .crawler import get_adverts_by_url, calculate_total_amount
from .fromownerdotcom import *
from .mycardotcom import *
from .db import *


def save(average_amount, input_link):
    link = get_link(input_link)
    save_or_update_statistic(average_amount, input_link, link)


def analyze(input_link, input_page_choice):
    total_adverts, total_amount = analyze_page(input_link, input_page_choice)
    average_amount = calculate(total_adverts, total_amount)
    return average_amount


def calculate(total_adverts, total_amount):
    average_amount = float(total_amount / len(total_adverts))
    return average_amount


def analyze_page(input_link, input_page_choice):
    logger.info(
        'Link : {link}, page_choice: {page_choice}'.format(link=input_link, page_choice=input_page_choice))
    parser = MyCarDotCom()
    total_adverts = get_adverts_by_url(parser, input_link, input_page_choice)
    total_amount = calculate_total_amount(total_adverts)
    logger.info(
        'total_amount : {total_amount} , total_adverts : {total_adverts}'.format(total_amount=total_amount,
                                                                                 total_adverts=total_adverts))
    return total_adverts, total_amount
