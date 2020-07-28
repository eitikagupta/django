from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('htmlpage',views.htmlpage),
    path('about',views.about),
    path('contact',views.contact),
    path('table',views.table,name="table"),
    path('login',views.login,name="login"),
    path('form',views.form,name="form"),
]