from django.shortcuts import render
# from django.urls import path
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("this is the home page!")

# def room(request):
#     return HttpResponse("this is the room page!")

rooms = [
    {'id':1, 'title':'Linear Algebra'},
    {'id':2, 'title':'AI'},
    {'id':3, 'title':'DataBase'},
]

def home(request):
    # render output should be like this : render(request, template_name, context)
    # which context should be dictionary
    context = {
        'rooms' : rooms
    }
    # separated the templates of base app from the main templates folder
    # we should mention 'base' because home.html is a template of base app
    return render(request, 'base/home.html', context)

def room(request, pk):
    final_room = None
    for room in rooms:
        # in dictionaries to get the value of a key : room['id'] or room.get('id')
        if room.get('id') == int(pk):
            final_room = room
    context = {
        'room' : final_room
    }
    return render(request, 'base/room.html', context)