from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Index Page Loaded')


def january(request):
    return HttpResponse('January Challenge')


def february(request):
    return HttpResponse('February Challenge')
