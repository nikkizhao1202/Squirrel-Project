from django.core.management.base import BaseCommand, CommandError
import datetime, csv
from sightings.models import Sightings
from django.apps import apps

class Command(BaseCommand):
    help = 'exports all information to csv files'

    def add_arguments(self, parser):
        parser.add_argument('website_path', type=str)

    def handle(self, *args, **options):
        with open(options['website_path'], 'w', newline='') as csvfile:
            model = squirrel_data
            field_names = [fa.name for fa in model._meta.fields]
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(field_names)
            for instance in model.objects.all():
                writer.writerow([getattr(instance, fi) for fi in field_names])
