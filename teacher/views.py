from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from student.models import *
 
def index(request):
    return HttpResponse("Welcome to View of Tec")
def about(request):
    return HttpResponse("Welcome to About of Tec")
def data(request):
    return render(request,"tech/data.html")
def addtec(request):
    return render(request,"tech/addtech.html")
def addtec1(request):
    if(request.method == "POST"):
        obj = Tec()
        obj.t_name = request.POST['t_name']
        obj.t_email = request.POST['t_email']
        obj.t_phone = request.POST['t_phone']
        obj.t_address = request.POST['t_address']
        obj.save()
    return redirect(addtec)
def alltec(request):
    data = Tec.objects.all()
    return render(request,"tech/alltec.html",{"data":data})
def search(request):
    if(request.method=="POST"):
        seaid = request.POST['id']
        data = Tec.objects.get(id=seaid)
        return render(request,"tech/search.html",{"data":data})
    else:
        return render(request,"tech/search.html")
def category(request):
    if(request.method=="POST"):
        cname = request.POST['cname']
        obj = Category()
        obj.name = cname
        obj.save()
        data = Category.objects.all()
        return render(request,"tech/category.html",{"data":data})        
    else:
        data = Category.objects.all()
        return render(request,"tech/category.html",{"data":data})
def subcat(request):
    if(request.method=="POST"):
        obj = Subcategory()
        #return HttpResponse(request.POST['cid']+request.POST['subcatname'])
        obj.cid = Category.objects.get(id=request.POST['cid'])
        obj.scname = request.POST['subcatname']
        
        obj.save()
        allcat = Category.objects.all()
        allsubcat = Subcategory.objects.all()
        return render(request,"tech/subcat.html",{"allcat":allcat,"allsubcat":allsubcat})
    else:
        allcat = Category.objects.all()
        allsubcat = Subcategory.objects.all()
        return render(request,"tech/subcat.html",{"allcat":allcat,"allsubcat":allsubcat})