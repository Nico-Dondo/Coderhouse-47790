# core/views.py
from django.shortcuts import render

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def search(request):
    # Lógica de búsqueda aquí
    return render(request, "core/search_results.html")
