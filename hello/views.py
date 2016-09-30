from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .forms import NameForm

# Create your views here.

def learn(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'learn.html')

def dl(request):
    # return HttpResponse('Hello from Python!')
    return HttpResponse('<pre>' + 'going to show hand writing weight and bias (test from j)' + '</pre>')


def index (request):
    return render(request, 'index.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def your_name(request):
    # return HttpResponse('Hello from Python!')
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid ():
            name = form.cleaned_data['your_name']
            #print form.cleaned_data
            #print name
            return HttpResponse (name)
        else :
            return HttpResponse ('/post, not valid form/')
    return HttpResponse('Error')
