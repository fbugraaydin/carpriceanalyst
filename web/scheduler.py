import schedule
import time
from .db import get_all_link
from .analyzer import analyze, save
from .scheduler import schedule_job

schedule_job()


def job():
    links = get_all_link()
    for link in links:
        average_amount = analyze(link, 1)
        save(average_amount, link)


def schedule_job():
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
