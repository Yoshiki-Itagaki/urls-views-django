from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def january(request):
    print(request)
    return HttpResponse("Eat no meat for the entire month!")

def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")

def march(request):
    return HttpResponse("Learn Django for at least 30 miniutes per day")

def get_month_by_number(request, month):
    return HttpResponse(month)

def get_month(request, month):
    if month == "january":
        msg = "Eat no meat for the entire month!" 
    elif month == "february":
        msg = "Walk for at least 20 minutes every day!"
    elif month == "march":
        msg = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")        
        
    return HttpResponse(msg)