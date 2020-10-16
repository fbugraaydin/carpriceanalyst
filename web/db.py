from .models import *
from datetime import date
import logging


def save_or_update_statistic(average_amount, input_link, link):
    today = date.today()
    statistic = Statistic.objects.filter(date=today, link__link=input_link)
    if len(statistic) == 1:
        statistic.update(average_amount=average_amount)
    else:
        statistic = Statistic(date=today, link=link, average_amount=average_amount)
        statistic.save()
    logging.info("Saved : {link}, averageAmount: {average_amount} ".format(link=link, average_amount=average_amount))


def get_link(input_link):
    link = Link.objects.filter(link=input_link)
    if link is None or len(link) == 0:
        return Link.objects.create(link=input_link)
    return link[0]


def get_all_link():
    return Link.objects.values_list('link', flat=True)
