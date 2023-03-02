from django.shortcuts import render
from django.http import HttpResponse
from requests import request

from django.http import HttpResponse
import requests
import ffmpy

# ai page links
def aione(request):
    return render(request , 'index.html')

def aiservice(request):
    return render(request , 'services.html')

def aicontact(request):
    return render(request , 'contact.html')

def aiabout(request):
    return render(request , 'about.html')

def homep(request):
    return render(request , 'index.html')
