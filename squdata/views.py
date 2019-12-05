from django.shortcuts import render
from .models import Squirreldata
from django.shortcuts import get_object_or_404, render, redirect
from .forms import SquirrelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
            return redirect("/sightings/add")
    else:
        form = SquirrelForm()
    return render(request, 'squdata/add.html', {'form':form})

