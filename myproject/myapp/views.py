from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person

people = []

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_person = Person(username=username, password=password)
        people.append(new_person)
        return HttpResponseRedirect('/')
    return render(request, 'add.html')

def index(request):
    return render(request, 'index.html', {'people': people})

