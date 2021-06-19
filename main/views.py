from django.shortcuts import render, redirect
from .models import ShortRoutes
from .models import MediumRoutes
from .models import LongRoutes
from .models import LongRunRoutes
from .models import DestinationRoutes

# Create your views here.
def home(request):

    return render(request, "main/home.html", {})

def short(request):
    routes = ShortRoutes.objects.all()

    return render(request, "main/short.html", {'routes':routes})

def medium(request):
    routes = MediumRoutes.objects.all()

    return render(request, "main/medium.html", {'routes':routes})

def long(request):
    routes = LongRoutes.objects.all()

    return render(request, "main/long.html", {'routes':routes})

def truelyLong(request):
    routes = LongRunRoutes.objects.all()

    return render(request, "main/truelyLong.html", {'routes':routes})

def destination(request):
    routes = DestinationRoutes.objects.all()

    return render(request, "main/destination.html", {'routes':routes})
