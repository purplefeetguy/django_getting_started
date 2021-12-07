from django.shortcuts import render
from django.http import HttpResponse

def welcom(request):
    return HttpResponse("Welcome to the Meeting Planner!")
