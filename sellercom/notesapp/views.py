from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Welcome to Django Project!")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def notes(request):
    return render(request,'notes.html')

def profile(request):
    return render(request,'profile.html')