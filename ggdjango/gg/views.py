from django.shortcuts import render
from .models import GGmomo

# Create your views here.
def all_gg(request):
    momos = GGmomo.objects.all()
    return render(request, 'gg/all_gg.html', {'momos': momos})