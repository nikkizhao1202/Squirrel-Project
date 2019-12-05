from django.utils.translation import gettext as _
from django.db import models
from django.urls import reverse


class Squirreldata(models.Model):

    longitude = models.CharField(
        help_text=('longitude'),
        max_length=17,
    )

    latitude = models.CharField(
        help_text=('latitude'),
        max_length=16,
    )


    unique_squirrel_id = models.CharField(
        help_text=('unique tag for each squirrel'),
        max_length=14,
        primary_key=True,
    )
    

    shift = models.CharField(
        help_text=('morning or late afternoon'),
        max_length=2,
        blank = True,
    )

    date = models.DateTimeField(
        help_text=('Concatenation of the sighting session day and month'),
        max_length=20,
    )

    age = models.CharField(
        help_text=_("Squirrel's age"),
        max_length=8,
        blank=True,
    )


    fur_color = models.CharField(
        help_text=_('Squirrel Primal Fur Color'),
        max_length=8,
        blank=True,
    )
    

    location = models.CharField(
        help_text=_('Location'),
        max_length=12,
        blank=True,
    )

    specific_location = models.CharField(
        help_text=_('Specific Location'),
        max_length=102,
        blank=True,
    )

    running = models.BooleanField(
        help_text=_('Running'),
        default=False,
    )

    chasing = models.BooleanField(
        help_text=_('Chasing'),
        default=False,
    )

    climbing = models.BooleanField(
        help_text=_('Climbing'),
        default=False,
    )

    eating = models.BooleanField(
        help_text=_('Eating'),
        default=False,
    )

    foraging = models.BooleanField(
        help_text=_('Foraging'),
        default=False,
    )

    other_activities = models.CharField(
        help_text=_('Other Activities'),
        max_length=140,
        blank=True,
    )

    kuks = models.BooleanField(
        help_text=_('Kuks'),
        default=False,
    )

    quaas = models.BooleanField(
        help_text=_('Quaas'),
        default=False,
    )

    moans = models.BooleanField(
        help_text=_('Moans'),
        default=False,
    )

    tail_flags = models.BooleanField(
        help_text=_('Tail flags'),
        default=False,
    )

    tail_twitches = models.BooleanField(
        help_text=_('Tail twitches'),
        default=False,
    )

    approaches = models.BooleanField(
        help_text=_('Approaches'),
        default=False,
    )

    indifferent = models.BooleanField(
        help_text=_('Indifferent'),
        default=False,
    )

    runs_from = models.BooleanField(
        help_text=_('Runs from'),
        default=False,
    )

    def __str__(self):
        return self.unique_squirrel_id 
    
    def get_absolute_url(self):
        return ('squirrel detail', (),
                {
                   'id': self.unique_squirrel_id,
                })
# Create your models here.
