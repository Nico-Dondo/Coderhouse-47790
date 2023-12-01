# core/urls.py
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="index"),
    path("about/", views.about, name="about"),
    path("search/", views.search, name="search"),  # Agrega esta línea
]
