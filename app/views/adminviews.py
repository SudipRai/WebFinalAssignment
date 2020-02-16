from django.shortcuts import render,redirect

# Create your views here.
from app.models.models import User
from app.forms.adminform import UserForm 
from django.http import HttpResponse
from django.contrib import messages
from app.authenticate import Authenticate


def login(request):
	return render(request,'adminlogin.html')

@Authenticate.valid_user
def index(request):
	users=User.objects.all()
	return render(request,"admindetail.html",{'users':users})

@Authenticate.valid_user
def create(request):
	if request.method=="POST":
		form=UserForm(request.POST,request.FILES)
		form.save()
		return redirect('/')


	form=UserForm()
	return render(request,"admin.html",{'form':form})


def entry(request):
	request.session['email']=request.POST['email']
	request.session['password']=request.POST['password']
	return redirect('/')

def logout(request):
	del request.session['email']
	del request.session['password']
	return redirect('/adminlogin')