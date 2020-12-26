from django.shortcuts import render
from django.http import HttpResponse

from .models import Country

def index(request):
    countries_list = Country.objects.order_by('-area')[:3]
    context = { 
        'countries_list': countries_list
    }
    return render(request, "polls/index.html", context)

def detail(request, id):
    certain_country = Country.objects.filter(id=id).first()
    context = {
        'certain_country': certain_country
    }
    return render(request, "polls/detail.html", context)

