from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hi Welcome to my blog home page")

def about(request):
    return HttpResponse("This is About Page")

def about(request):
    a = 10+50
    return HttpResponse("This is About Page:{60}")