from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [ 
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path("ch1/", views.ch1, name='ch1'),
    path("ch2/", views.ch2, name='ch2'),
]
