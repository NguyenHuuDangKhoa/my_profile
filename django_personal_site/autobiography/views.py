from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'autobiography/home.html', {'title': "Home"})

def resume(request):
    return render(request, 'autobiography/resume.html', {'title': "Resume"})