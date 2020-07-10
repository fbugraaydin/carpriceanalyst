from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .db import get_all_link
from .analyzer import analyze, save
import logging

logger = logging.getLogger(__name__)


def job():
    links = get_all_link()
    for link in links:
        average_amount = analyze(link.link, 1)
        save(average_amount, link.link)


def schedule_job():
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(job, CronTrigger(hour=9, minute=5))
    scheduler.start()