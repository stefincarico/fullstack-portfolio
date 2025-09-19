# pages/views.py
from django.shortcuts import render # Cambiamo l'import

def home_page_view(request):
    return render(request, "home.html") # Usiamo render

def about_page_view(request):
    return render(request,"about.html")