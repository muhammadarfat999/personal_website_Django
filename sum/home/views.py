from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    person = {
        'name':'Muhammad Arfat', 'age':22
        }
            
    return render(request,'base/index.html', person)