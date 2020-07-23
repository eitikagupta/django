from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello From Index Ji")

def about(request):
    return HttpResponse("Hello From About Page--")
def contact(request):
    a = 10
    b = 20
    c=  a+b
    return HttpResponse("Hey Buddy Welcome to Contact Page"+str(c))
