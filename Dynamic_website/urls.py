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

urlpatterns = [
    path('home',productviews.home),
    path('srch',productviews.search),
    path('',productviews.index),
    path('edit/<int:id>',productviews.edit),
    path('update/<int:id>',productviews.update),
    path('delete/<int:id>',productviews.delete),
    path('create',productviews.create),
    path('signup',customerviews.create),
    path('customerdetail',customerviews.index),
    path('admin',adminviews.create),
    path('admindetail',adminviews.index), 
    path('adminlogin',adminviews.login),
    path('entry',adminviews.entry), 
    path('entryhome',customerviews.entry),
    path('login',customerviews.login),  

]
