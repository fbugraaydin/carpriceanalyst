from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from web.db import get_all_link
from web.analyzer import analyze, save
import logging

logger = logging.getLogger(__name__)


def job():
    links = get_all_link()
    for link in links:
        try:
            average_amount = analyze(link, 1)
            save(average_amount, link)
        except Exception as e:
            logger.error(e)


def schedule_job():
    logger.info("Scheduler is being started by Heroku!")
    job()
    # scheduler = BackgroundScheduler(daemon=True)
    # scheduler.add_job(job, CronTrigger(hour=17, day='*', minute=20))
    # scheduler.start()
