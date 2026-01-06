from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hi Welcome to my blog home page")

def about(request):
    return HttpResponse("This is About Page")