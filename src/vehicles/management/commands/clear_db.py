from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    def handle(self, *args, **options):
        app = apps.get_app_config('vehicles')
        for model in app.models.values():
            model.objects.all().delete()

        app = apps.get_app_config('history')
        for model in app.models.values():
            model.objects.all().delete()
