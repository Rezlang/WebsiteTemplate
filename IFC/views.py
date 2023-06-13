from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'IFC/homepage.html')


def leadership(request):
    return render(request, 'IFC/leadership.html')


def contacts(request):
    return render(request, 'IFC/contacts.html')


def ourChapters(request):
    return render(request, 'IFC/ourChapters.html')


def schedule(request):
    return render(request, 'IFC/schedule.html')


def title9(request):
    return render(request, 'IFC/title9.html')


def forChapters(request):
    return render(request, 'IFC/forChapters.html')


def aboutUs(request):
    return render(request, 'IFC/aboutUs.html')


def calendar(request):
    return render(request, 'IFC/calendar.html')
