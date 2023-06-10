from django.urls import path
from IFC import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("", views.contacts, name="contacts"),
    path("", views.ourChapters, name="ourChapters"),
    path("", views.forChapters, name="forChapters"),
    path("", views.title9, name="title9"),
    path("leadership", views.leadership, name="title9"),
]
