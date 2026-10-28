from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse("Hello, World!. You are at ggdjango home page")
    return render(request, 'website/index.html')

def about(request):
    #return HttpResponse("Hello, World!. You are at ggdjango about page")
    return render(request, 'website/about.html')

def contact(request):
    #return HttpResponse("Hello, World!. You are at ggdjango contact page")
    return render(request, 'website/contact.html')