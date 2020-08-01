from django.urls import path,include
from . import views
from django.conf.urls.static import *

urlpatterns = [
    path('',views.index),
    path('templateindex',views.templateindex),
    path('htmlpage',views.htmlpage),
    path('about',views.about),
    path('contact',views.contact),
    path('table',views.table,name="table"),
    path('login',views.login,name="login"),
    path('form',views.form,name="form"),
]