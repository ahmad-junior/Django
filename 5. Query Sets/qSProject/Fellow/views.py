from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):
    item_search = "Muhammad Ahmad"
    item_found = Member.objects.filter(name=item_search)
    members = Member.objects.all()
    params = {'members': members, 'item_search': item_search, 'search_item': item_found}
    return render(request, 'index.html', params)
