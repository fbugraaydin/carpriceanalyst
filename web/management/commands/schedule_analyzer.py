from django.core.management.base import BaseCommand
from web.scheduler import schedule_job


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        schedule_job()
