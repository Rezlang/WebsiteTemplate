from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'homepage/homepage.html')


def contacts(request):
    return render(request, 'homepage/contacts.html')


def ourChapters(request):
    return render(request, 'homepage/ourChapters.html')


def schedule(request):
    return render(request, 'homepage/schedule.html')


def title9(request):
    return render(request, 'homepage/title9.html')


def forChapters(request):
    return render(request, 'homepage/forChapters.html')


def aboutUs(request):
    return render(request, 'homepage/aboutUs.html')


def ourChapters(request):
    return render(request, 'homepage/ourChapters.html')
