from django.shortcuts import render

# Create your views here.
from .models import *

def index (request):
    num_films = Film.objects.all().count()
    num_directors = Director.objects.all().count()

    return render(request, 'index.html', context={'num_films': num_films, 'num_directors': num_directors})