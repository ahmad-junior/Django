from django.shortcuts import render
from .models import MyFellows

def main(request):
    return render(request, "main.html")

def index(request):
    members = MyFellows.objects.all().values()
    params = {'members': members}
    return render(request, 'index.html', params)

def details(request, id):
    friend = MyFellows.objects.all().values().get(id=id)
    params = {'friend': friend}
    return render(request, 'details.html', params)

def test(request):
    params = {'title': 'Testing our template', 'fruits': ['apple', 'banana', 'orange']}
    return render(request, 'template.html', params)
