from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def store(request):
    context = {}
    return HttpResponse("hello world")