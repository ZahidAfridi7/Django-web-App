from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect


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
    "dec": "this for December"   
}

def all_months(request, month):
    try:
        text = all_month_name[month]
        return HttpResponse(text)
    except:
        HttpResponseNotFound("invalid entery!")
    
    
def all_months_by_num(request, month):
    months = list(all_month_name.keys())
    
    if month > len(months):
        return HttpResponseNotFound("invalid entery")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/webpage/" + redirect_month)
    
    
    