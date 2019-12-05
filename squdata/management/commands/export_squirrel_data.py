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
            field_names = [latitude,
                        longitude,
                        unique_squirrel_id,
                        shift,
                        date,
                        age,
                        fur_color,
                        location,
                        specific_location,
                        running,
                        chasing,
                        climbing,
                        eating,
                        foraging,
                        other_activities,
                        kuks,
                        quaas,
                        moans,
                        tail_flags,
                        tail_twitches,
                        approaches,
                        indifferent,
                        runs_from]
            writer = csv.writer(csvfile)
            writer.writerow(field_names)
            for instance in model.objects.all():
                writer.writerow([getattr(instance, fi) for fi in field_names])
