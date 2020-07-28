from django.shortcuts import render,redirect
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

def htmlpage(request):
    return render(request,"student/page.html")
def table(request):
    uname = request.POST['uname']
    return render(request,"student/table.html",{"name":uname})
def login(request):

    return render(request,"student/login.html")
def form(request):
    if(request.method=="POST"):
       data = int(request.POST['data'])
       temp=[]
       for i in range(0,data):
           temp.append(i)
       return render(request,"student/formhandle.html",{"myvar":temp})
    else:
        return render(request,"student/form.html")