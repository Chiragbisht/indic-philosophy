
from django.shortcuts import render



def home(request):
    return render(request, 'timeline/home.html')

def indic_philosophy(request):
    return render(request, 'timeline/indic_philosophy.html')