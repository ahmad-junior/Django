from django.shortcuts import render

def index(request):
    params = {'name': "Muhammad Ahmad", 'age': 20}
    return render(request, 'index.html', params)