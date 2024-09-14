from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenges = {
    "january": "january".capitalize() + ": Eat no meat for the entire month!" ,
    "february": "february".capitalize() + ": Walk for at least 20 minutes every day!",
    "march": "march".capitalize() + ": Learn Django for at least 20 minutes every day!",
    "april": "april".capitalize() + ": Eat no meat for the entire month!" ,
    "may": "may".capitalize() + ": Walk for at least 20 minutes every day!",
    "june": "june".capitalize() + ": Learn Django for at least 20 minutes every day!",
    "july": "july".capitalize() + ": Eat no meat for the entire month!" ,
    "august": "august".capitalize() + ": Walk for at least 20 minutes every day!",
    "september": "september".capitalize() + ": Learn Django for at least 20 minutes every day!",
    "october": "october".capitalize() + ": Eat no meat for the entire month!" ,
    "november": "november".capitalize() + ": Walk for at least 20 minutes every day!",
    "december": "december".capitalize() + ": Learn Django for at least 20 minutes every day!",
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    responseData = f"<ul>{list_items}</ul>"
    return HttpResponse(responseData)

def get_month_by_number(request, month):
    months = list(challenges.keys())
        
    if month == 0 or month > len(months):
        return HttpResponse("Invalid month")
            
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def get_month(request, month):
    try:
        msg = challenges[month]
        response_data = f"<h1>{msg}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponse("<h1>This month is not supported!</h1>")
        
    