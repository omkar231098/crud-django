# crud_app/views.py
from django.shortcuts import render, redirect
from .models import Person

def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        person = Person(name=name, age=age, city=city)
        person.save()
        return redirect('index')
    return render(request, 'create.html')

def update(request, person_id):
    person = Person.objects.get(pk=person_id)
    if request.method == 'POST':
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.city = request.POST.get('city')
        person.save()
        return redirect('index')
    return render(request, 'update.html', {'person': person})

def delete(request, person_id):
    person = Person.objects.get(pk=person_id)
    if request.method == 'POST':
        person.delete()
        return redirect('index')
    return render(request, 'delete.html', {'person': person})
