import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Akshay Sharma'})

def add(request):
    value1=int(request.POST['num1'])
    value2=int(request.POST['num2'])
    res=value1+value2
    return render(request,'result.html',{'result':res})