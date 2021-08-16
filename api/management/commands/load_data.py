import csv

from django.conf import settings
from django.core.management import BaseCommand
from api.models import Shop


class Command(BaseCommand):
    help = 'Load data from csv files'

    def handle(self, *args, **kwargs):
        with open(
            f'{settings.BASE_DIR}/static/data/shop_metrics.csv',
            'r', encoding='utf-8'
        ) as csv_file:
            reader = csv.DictReader(csv_file)
            Shop.objects.bulk_create(Shop(**data) for data in reader)

        self.stdout.write(self.style.SUCCESS('Successfully load data'))
