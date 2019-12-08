from django.shortcuts import render
from .models import Squirreldata
from django.shortcuts import get_object_or_404, render, redirect
from .forms import SquirrelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
# Create your views here.
def sightings(request):
    sqd = Squirreldata.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(sqd, 20)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'squdata/sightings.html', {'users':users})


def add(request):
    if request.method == "POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/squdata/sightings/add")
    else:
        form = SquirrelForm()
    return render(request, 'squdata/add.html', {'form':form})

def edit(request, unique_squirrel_id):
    edit_instance = Squirreldata.objects.get(unique_squirrel_id = unique_squirrel_id)
    if request.method == "POST":
        form = SquirrelForm(request.POST, instance = edit_instance)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = SquirrelForm(instance = edit_instance)
    return render(request, 'squdata/edit.html', {'form': form, 'unique_squirrel_id':unique_squirrel_id})

def stats(request):
    squirrels = Squirreldata.objects.all()
    total = len(squirrels)
    running = squirrels.values_list('running').annotate(Count('running'))
    shift = squirrels.values_list('shift').annotate(Count('shift'))
    climbing = squirrels.values_list('climbing').annotate(Count('climbing'))
    eating = squirrels.values_list('eating').annotate(Count('eating'))
    foraging = squirrels.values_list('foraging').annotate(Count('foraging'))
    context = {'total': total,
		'running': running,
		'shift': shift,
		'climbing': climbing,
		'eating': eating,
		'foraging': foraging,
		}
    return render(request, 'squdata/stats.html', {'squirrels':squirrels})

