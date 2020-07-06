from django.apps import AppConfig


class WebConfig(AppConfig):
    name = 'web'

    def ready(self):
        from .scheduler import schedule_job
        schedule_job()
