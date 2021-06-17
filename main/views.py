from django.shortcuts import render, redirect


# Create your views here.
def home(request):

    return render(request, "main/home.html", {})

def short(request):

    return render(request, "main/short.html", {})

def medium(request):

    return render(request, "main/medium.html", {})

def long(request):

    return render(request, "main/long.html", {})

def truelyLong(request):

    return render(request, "main/truelyLong.html", {})

def destination(request):

    return render(request, "main/destination.html", {})
