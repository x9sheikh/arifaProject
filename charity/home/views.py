from django.shortcuts import render
from django.http import *
# Create your views here.
def home_view(request):
    context={

    }
    return render(request, 'base.html', context=context)
