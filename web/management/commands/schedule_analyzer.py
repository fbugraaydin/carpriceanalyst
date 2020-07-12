from django.core.management.base import BaseCommand
from web.scheduler import job


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        job()
