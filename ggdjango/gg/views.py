from django.shortcuts import render
from .models import GGmomo
from django.shortcuts import get_object_or_404

# Create your views here.
def all_gg(request):
    momos = GGmomo.objects.all()
    return render(request, 'gg/all_gg.html', {'momos': momos})

def gg_detail(request,momo_id):
    momo = get_object_or_404(GGmomo, pk=momo_id)
    return render(request, 'gg/gg_detail.html',{'momo':momo})