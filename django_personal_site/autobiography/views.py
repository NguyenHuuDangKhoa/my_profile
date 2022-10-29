from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'autobiography/home.html')

def resume(request):
    return HttpResponse('<h1>Resume</h1>')