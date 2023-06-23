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


def documents(request):
    return render(request, 'IFC/importantDocuments.html')


def forChapters(request):
    return render(request, 'IFC/forChapters.html')


def constitution(request):
    return render(request, 'IFC/constitution.html')


def calendar(request):
    return render(request, 'IFC/calendar.html')


def register(request):
    return render(request, 'IFC/register.html')


def fall(request):
    return render(request, 'IFC/fall.html')


def spring(request):
    return render(request, 'IFC/spring.html')


def eventSchedule(request):
    return render(request, 'IFC/eventSchedule.html')
