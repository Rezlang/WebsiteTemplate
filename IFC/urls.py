from django.urls import path
from IFC import views

urlpatterns = [
    path("", views.homepage, name="home"),
]
