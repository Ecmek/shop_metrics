import os

import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dataset_task.settings")
django.setup()
from api.models import Shop # noqa


def main():
    df = pd.read_csv(
        'https://gist.githubusercontent.com/artrey/8d6a3f2d91cefb5e6343bedbc9ef8c79/raw/'
        '4cd7c3c7cfbc4c288b4df984611479550a0fdbf9/dataset.csv',
        delimiter=',',
    )
    dataset = [
        Shop(
            date=df.iloc[row][0],
            shop=df.iloc[row][1],
            country=df.iloc[row][2],
            visitors=df.iloc[row][3],
            earnings=df.iloc[row][4]

        )
        for row in range(df.count()[0])
    ]
    Shop.objects.bulk_create(dataset)


if __name__ == '__main__':
    main()
