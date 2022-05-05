from django.shortcuts import render

from travello.models import destination

# Create your views here.
def index(request):
    dests = destination.objects.all()
    return render(request, 'index.html',{'d':dests})