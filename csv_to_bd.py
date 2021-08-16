import os
import csv

import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop_metrics.settings")
django.setup()
from api.models import Shop # noqa

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    df = pd.read_csv(
        f'{BASE_DIR}/static/data/shop_metrics.csv', delimiter=',',
    )
    shop_metrics = [
        Shop(
            date=df.iloc[row][0],
            shop=df.iloc[row][1],
            country=df.iloc[row][2],
            visitors=df.iloc[row][3],
            earnings=df.iloc[row][4]

        )
        for row in range(df.count()[0])
    ]
    Shop.objects.bulk_create(shop_metrics)


if __name__ == '__main__':
    main()
