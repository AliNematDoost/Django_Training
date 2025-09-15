from django.shortcuts import render
# from django.urls import path
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("this is the home page!")

# def room(request):
#     return HttpResponse("this is the room page!")

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')