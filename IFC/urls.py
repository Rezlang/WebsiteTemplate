from django.urls import path
from IFC import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("documents", views.documents, name="documents"),
    path("chapters", views.ourChapters, name="chapters"),
    path("calendar", views.calendar, name="calendar"),
    path("constitution", views.constitution, name="constitution"),
    path("leadership", views.leadership, name="leadership"),
]
