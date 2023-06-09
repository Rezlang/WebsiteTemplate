from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'title': 'Welcome to My Website',
        'content': 'This is the homepage of my sample website.',
    }
    return render(request, 'homepage/index.html', context)


def contacts(request):
    return HttpResponse("Test")
