from django.shortcuts import render
from .models import Fellow

# Create your views here.
def index(request):
    members = Fellow.objects.all().values()
    params = {'members': members}
    return render(request, 'index.html', params)