from django.shortcuts import render
from django.http import *
# Create your views here.
def home_view(request,'home/home.html'):
    return HttpResponse("this is home page");
