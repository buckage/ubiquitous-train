from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    now = datetime.datetime.now()

    context = {
        'time': now
    }
    return(render(request, 'app/home.html', context))