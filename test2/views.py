from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def defult(request):
    return HttpResponse('test2/defult site')

def my1(resquest):
    return HttpResponse('Welcome bro you are now in test2 app')