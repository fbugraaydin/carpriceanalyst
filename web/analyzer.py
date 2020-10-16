from .crawler import get_adverts_by_url, calculate_total_amount
from .fromownerdotcom import *
from .mycardotcom import *
from .db import *
import logging

def save(average_amount, input_link):
    link = get_link(input_link)
    logging.info("Saving : {link}, averageAmount: {} ".format(link=link, average_amount=average_amount))
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
    parser = get_parser(input_link)

    total_adverts = get_adverts_by_url(parser, input_link, input_page_choice)
    total_amount = calculate_total_amount(total_adverts)
    logger.info(
        'total_amount : {total_amount} , total_adverts : {total_adverts}'.format(total_amount=total_amount,
                                                                                 total_adverts=len(total_adverts)))
    return total_adverts, total_amount


def get_parser(input_link):
    if "sahibinden.com" in input_link:
        return FromOwnerDotCom()
    else:
        return MyCarDotCom()
