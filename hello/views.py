from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.

def dl(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def index (request):
    return HttpResponse('<pre>' + 'ML2016CSWZ, gang chen say hello, gordon' + '</pre>')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
