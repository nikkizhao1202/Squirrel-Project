import os
import csv 
import datetime as dt
from squdata.models import Squirreldata
from django.core.management.base import BaseCommand, CommandError
import pytz #pip install pytz

# from django.utils.timezone import get_current_timezone
class Command(BaseCommand):
    help = 'read csv file'
    
    def add_arguments(self, parser):
        parser.add_argument('squ_file',type=str) 
    
    def handle(self, *args, **options):
        def tobool(string):
            if string == 'true':
                return True
            elif string == 'false':
                return False 


        file_path = options['squ_file']
        with open(file_path, 'r', encoding='UTF-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for col in csv_reader:
                lat = col[0]
                lon = col[1]
                squ_id = col[2]
                shift = col[4]
                timezone = pytz.timezone("UTC")
                date = dt.datetime.strptime(col[5],'%m%d%Y')
                date = timezone.localize(date)
                age = col[7]
                fur_color = col[8]
                location = col[12]
                specific_location = col[14]
                running = tobool(col[15])
                chasing = tobool(col[16])
                climbing = tobool(col[17])
                eating = tobool(col[18])
                foraging = tobool(col[19])
                other_activities = col[20]
                kuks = tobool(col[21])
                quaas = tobool(col[22])
                moans = tobool(col[23])
                tail_flag = tobool(col[24])
                tail_twitch = tobool(col[25])
                approach =  tobool(col[26])
                indifferent = tobool(col[27])
                runs_from = tobool(col[28])

                try:
                    _,created = Squirreldata.objects.get_or_create(
                            latitude=lat,
                            longitude=lon,
                            unique_squirrel_id=squ_id,
                            shift=shift,
                            date=date,
                            age=age,
                            fur_color=fur_color,
                            location=location,
                            specific_location=specific_location,
                            running=running,
                            chasing=chasing,
                            climbing=climbing,
                            eating=eating,
                            foraging=foraging,
                            other_activities=other_activities,
                            kuks=kuks,
                            quaas=quaas,
                            moans=moans,
                            tail_flags=tail_flag,
                            tail_twitches=tail_twitch,
                            approaches=approach,
                            indifferent=indifferent,
                            runs_from=runs_from,
                        )
                   
                except FileNotFoundError:
                    raise CommandError("File {} does not exist".format(file_path))
