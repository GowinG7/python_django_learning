from django.shortcuts import render

# Create your views here.
def all_gg(request):
    return render(request,'gg/all_gg.html')