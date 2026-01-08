from django.http import HttpResponse

def home(request):
    return HttpResponce("Shop Home Page")

def products(request):
    return HttpResponse("Shop products Page")
