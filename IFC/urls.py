from django.urls import path
from IFC import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("", views.contacts, name="contacts"),
    path("chapters", views.ourChapters, name="chapters"),
    path("calendar", views.calendar, name="calendar"),
    path("", views.title9, name="title9"),
    path("leadership", views.leadership, name="leadership"),
]
