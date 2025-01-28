from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Django Web Application!</h1>")

def game(request):
    return render(request, 'game.html')