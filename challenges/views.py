from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenges = {
    "january": "Eat no meat for the entire month!" ,
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!" ,
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!" ,
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!" ,
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!",
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
        return render(request, "challenges/challenge.html", {
            "text": msg,
            "month_name": month

        })
    except:
        return HttpResponse("<h1>This month is not supported!</h1>")
        
    