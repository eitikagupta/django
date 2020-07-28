from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to View of Tec")
def about(request):
    return HttpResponse("Welcome to About of Tec")
def data(request):
    return render(request,"tech/data.html")