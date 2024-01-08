from django.shortcuts import render
from .models import About

# Create your views here.
def index(request):
    about = About.objects.get() 

    context= {
        'about': about,
    }
    return render(request, 'index.html',context)