from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Index Page Loaded')


# def january(request):
#     return HttpResponse('January Challenge')


# def february(request):
#     return HttpResponse('February Challenge')

def month_function(request, month):
    month_text = None
    if(month == 'january'):
        month_text = "Welcome to january"
    else:
        return HttpResponseNotFound('Month is not recognized!')
    return HttpResponse(month_text)
