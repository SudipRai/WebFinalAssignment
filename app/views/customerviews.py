from django.shortcuts import render,redirect
from app.models.products import Customer
from app.models.products import Product
from app.forms.customerforms import CustomerForm
from django.http import HttpResponse
from app.authenticate import Authenticate,AuthenticateC


@Authenticate.valid_user
def index(request):
	customers=Customer.objects.all()
	return render(request,"customerdetail.html",{'customers':customers})



def create(request):
	if request.method=="POST":
		form=CustomerForm(request.POST,request.FILES)
		form.save()
		return redirect('/home')


	form=CustomerForm()
	return render(request,"signup.html",{'form':form})

def entry(request):
	request.session['name']=request.POST['name']
	request.session['password']=request.POST['password']
	return redirect('/Shop')

@AuthenticateC.valid_customer	
def shop(request):
	products=Product.objects.all()
	return render(request,'Shop.html',{'products':products})

def login(request):
	return render(request,'login.html')

def logout(request):
	del request.session['name']
	del request.session['password']
	return redirect('/home')

def profile(request,name="request.session.name"):
	customer=Customer.objects.get(name=name)
	return render(request,'profile.html',{'customer':customer})

def delete(request,id):
	
	customer=Customer.objects.get(id=id)
	customer.delete()
	return redirect('/home')

def edit(request,id):
	customer=Customer.objects.get(id=id)
	return render(request,'customeredit.html',{'customer':customer})


def update(request,id):
	customer=Customer.objects.get(id=id)
	form=CustomerForm(request.POST,request.FILES,instance=customer)
	form.save()
	return redirect('/home')