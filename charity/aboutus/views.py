from django.shortcuts import render
from django.http import *


# Create your views here.
def aboutus_view(request):
    return HttpResponse('i am aboutus')