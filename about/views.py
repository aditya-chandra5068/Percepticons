from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def about(request):
    context = {
        'current_page':'about'
    }
    return render(request ,'about/about.html', context) 