from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .db import get_all_link
from .analyzer import analyze, save
import logging
import time

logger = logging.getLogger(__name__)


def job():
    links = get_all_link()
    for link in links:
        try:
            average_amount = analyze(link, 1)
            save(average_amount, link)
            time.sleep(60)
        except Exception as e:
            logger.error(e)


def schedule_job():
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(job, CronTrigger(hour=9))
    scheduler.start()
