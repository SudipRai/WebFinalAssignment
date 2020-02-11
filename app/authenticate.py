from django.shortcuts import redirect
from app.models.models import User
from app.models.models import Customer
from django.contrib import messages
from django.db.models import Q

# /*------------Authentication to for Back-End------------------*/
class Authenticate:
	def valid_user(function):
		def wrap(request):
			try:
				# User.objects.get(email=request.session['email'])
				User.objects.get(Q(password=request.session['password']) & Q(email=request.session['email']))
				return function (request)
			except:
				messages.warning(request,"Invalid email or password")
				return redirect('/adminlogin')
		return wrap
# /*----------------------Authentication for Front-end------------------------*/		
class AuthenticateC:
	def valid_customer(function):
		def wrap(request):
			try:
				# User.objects.get(email=request.session['email'])
				Customer.objects.get(Q(password=request.session['password']) & Q(name=request.session['name']))
				return function (request)
			except:
				messages.warning(request,"Invalid email or password")
				return redirect('/login')
		return wrap
