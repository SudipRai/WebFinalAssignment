from django.shortcuts import render,redirect
from app.models.products import Product
from app.forms.productforms import ProductForm
from app.authenticate import Authenticate,AuthenticateC
from django.http import HttpResponse,JsonResponse
# Create your views here.def index(request):

def home(request):
	return render(request,"home.html")


@Authenticate.valid_user

def index(request):
	limit=3
	page=1
	if request.method=="POST":
		if "next" in request.POST:
			page=(int(request.POST['page'])+1)
		elif "prev" in request.POST:
			page=(int(request.POST['page'])-1)
		tempoffset=page-1
		offset=tempoffset*page
		products=Product.objects.raw("select *from product limit 3 offset %s",[offset])
	else:
		products=Product.objects.raw("select *from product limit 3 offset 0")
	return render(request,"index.html",{'products':products,'page':page})


def search(request):
	products=Product.objects.filter(name__contains=request.GET['srch']).values()
	return JsonResponse(list(products),safe=False)


def create(request):

	if request.method=="POST":
		form=ProductForm(request.POST,request.FILES)
		form.save()
		return redirect('/')


	form=ProductForm()
	return render(request,'create.html',{'form':form})


def edit(request,id):
	product=Product.objects.get(id=id)
	return render(request,'edit.html',{'product':product})


def update(request,id):
	product=Product.objects.get(id=id)
	form=ProductForm(request.POST,request.FILES,instance=product)
	form.save()
	return redirect('/')


def delete(request,id):
	Product.objects.get(id=id).image.delete()
	product=Product.objects.get(id=id)
	product.delete()
	return redirect('/')