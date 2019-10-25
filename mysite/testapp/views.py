from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def testapp_index(request):
    return HttpResponse(" THis is a test view. same as polls - tutorial 1")