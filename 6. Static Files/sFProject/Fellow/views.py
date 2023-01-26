from django.shortcuts import render
from .models import Member

# Create your views here.
def welcome(request):
    return render(request, "home.html")

def mainDataBase(request):
    memebers = Member.objects.all()
    params = {"members":memebers}
    return render(request, "fellows.html", params)