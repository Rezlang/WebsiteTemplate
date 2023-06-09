from django.urls import path
from IFC import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("", views.contacts, name="home"),
    path("", views.ourChapters, name="home"),
    path("", views.forChapters, name="home"),
    path("", views.homepage, name="home"),
    path("", views.homepage, name="home"),
    path("", views.homepage, name="home"),
]
