from this import d
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello')

def my1(request):
    return HttpResponse('Hello Ediot')

def my2(request):
    return HttpResponse('Buonsoar Eliot')