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
    path('produts',views.produts,name="produts"),
    path('savepro',views.savepro,name="savepro"),
    path('viewproducts',views.viewproducts,name="viewproducts"),
    path('dele/<int:ids>',views.dele,name="dele"),
    path('updatepro',views.updatepro,name="updatepro"),
    path('updateform/<int:ids>',views.updateform,name="updateform")

]