import csv
from datetime import date
from itertools import islice
import pathlib
from django.conf import settings
from django.core.management.base import BaseCommand
from home.models import CO2

class Command(BaseCommand):
    help = 'Load data from CO2 file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'final_data.csv'

        with open(datafile, newline='') as csvfile:
            reader = csv.DictReader(islice(csvfile, 0, 100))
            for row in reader:
               
             CO2.objects.get_or_create(div=row['Division'], pmm=row['PM25'])
                

        