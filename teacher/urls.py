from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('data',views.data),
    path('addtec',views.addtec,name="addtec"),
    path('addtec1',views.addtec1,name="addtec1"),
    path('alltec',views.alltec,name="alltec"),
    path('search',views.search,name="search"),
    path('category',views.category,name="category"),
    path('subcat',views.subcat,name="subcat"),

]