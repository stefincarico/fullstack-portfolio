# pages/views.py
from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("<h1>Ciao Mondo! Questa è la homepage.</h1>")