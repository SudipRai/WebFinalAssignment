"""Dynamic_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import productviews
from app.views import customerviews
from app.views import adminviews
from app.views import orderviews

urlpatterns = [
    path('home',productviews.home),
    path('srch',productviews.search),
    path('',productviews.index),
    path('edit/<int:id>',productviews.edit),
    path('customeredit/<int:id>',customerviews.edit),
    path('customerupdate/<int:id>',customerviews.update),
    path('delete/<int:id>',productviews.delete),
    path('deletecustomer/<int:id>',customerviews.delete),
    path('create',productviews.create),
    path('signup',customerviews.create),
    path('customerdetail',customerviews.index),
    path('admin',adminviews.create),
    path('admindetail',adminviews.index), 
    path('adminlogin',adminviews.login),
    path('entry',adminviews.entry), 
    path('entryhome',customerviews.entry),
    path('login',customerviews.login), 
    path('logout',customerviews.logout),
     path('logoutadmin',adminviews .logout),
    path('profile/<str:name>',customerviews.profile), 
    path('Shop',customerviews.shop),
    path('orderdetail',orderviews.order),
    path('addorder',orderviews.create),
    path('order/<int:id>/<str:name>',orderviews.orderdetail),
    path('mycart/<str:name>',orderviews.mycart),
    path('deleteorder/<int:id>',orderviews.delete)
]
