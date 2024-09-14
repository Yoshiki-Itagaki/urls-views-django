from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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

def get_month_by_number(request, month):
    months = list(challenges.keys())
    
    print(months)
    
    if month == 0 or month > len(months):
        return HttpResponse("Invalid month")
            
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def get_month(request, month):
    try:
        msg = challenges[month]
        return HttpResponse(msg)
    except:
        return HttpResponse("This month is not supported")
        
    