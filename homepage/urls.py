from django.urls import path
from homepage import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/contacts", views.contacts, name="contacts"),
]
