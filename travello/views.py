from django.shortcuts import render
from .models import Destination

def index(request):
    dests=Destination.objects.all()
    #<img src="{{dest.img.url}}" alt="">

    return render(request,"index.html",{'dests':dests})