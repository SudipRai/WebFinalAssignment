from django.shortcuts import render,redirect
from app.models.models import Product,Customer,Order
from app.forms.productforms import ProductForm
from app.forms.orderform import OrderForm
from app.authenticate import Authenticate,AuthenticateC
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect




@Authenticate.valid_user
def order(request):
	orders=Order.objects.all()
	return render(request,"orderdetail.html",{'orders':orders})

		
	
def orderdetail(request,id,name="request.session.name"):
	customer=Customer.objects.get(name=name)
	product=Product.objects.get(id=id)
	return render(request,'orderform.html',{'product':product,'customer':customer})


def create(request):
	if request.method=="POST":
		form=OrderForm(request.POST)
		form.save()
		return redirect('/Shop')

def mycart(request,name="request.session.name"):
	orders=Order.objects.filter(customername=name)
	return render(request,'mycart.html',{'orders':orders})


def checkout(request,id):
	orders=Order.objects.get(orderid=id)
	return render(request,'checkout.html',{'orders':orders})

def delete(request,id):
	order=Order.objects.get(orderid=id)
	order.delete()
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deliver(request,id,name="request.session.name"):
	order=Order.objects.get(orderid=id,customername=name)
	order.delete()
	return redirect('/Shop')

