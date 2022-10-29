from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home</h1>')

def resume(request):
    return HttpResponse('<h1>Resume</h1>')