from django.shortcuts import render

from squdata.models import Squirreldata
# Create your views here.

def map(request):
    squirrels = Squirreldata.objects.all()[:100]
    context = {'squirrels': squirrels}
    return render(request, 'map/map.html', context)
