from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django!")


def contacts(request):
    return HttpResponse("Test")
