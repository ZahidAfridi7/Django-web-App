from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


# def jan(request):
#     return HttpResponse("hello this is januaray response")

# def feb(request):
#     return HttpResponse("this is request for februray")

all_month_name = {
   "jan" : "this for january",
    "feb": "this for february",
   "march": "this for march",
    "april" : "this for april",
    "may": "this for may",
    "june": "this for june",
    "july": "this for july",
    "august": "this is for august",
    "sept": "this for septemeber",
    "oct": "this for October",
    "nov":  "this for November",
    "dec": None   
}

def index(request):
    
    months = list(all_month_name.keys())
    return render(request, "webpage/index.html",
                  {
        "months" : months
    })
   

def all_months(request, month):
    try:
        text = all_month_name[month]
        return render(request, "webpage/webpage.html",{
            'text': text,
            'month_name': month
        })
        
    except KeyError:
        response_data = render_to_string("404.html")
    return HttpResponseNotFound(response_data)
    
    
def all_months_by_num(request, month):
    months = list(all_month_name.keys())
    
    if month > len(months):
        response_data = render_to_string("404.html")
    return HttpResponseNotFound(response_data)
        # return HttpResponseNotFound("<h1>invalid entery<h1>")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly-task", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    
    
    