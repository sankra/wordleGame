'''
This view has no much work to do.
It is looking for GET requests and it will display the h1 tag in one instance
and rendering game.html page in another instance.

'''

from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Django Web Application!</h1>")

def game(request):
    return render(request, 'game.html')
