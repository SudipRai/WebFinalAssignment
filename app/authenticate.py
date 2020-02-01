from django.shortcuts import redirect
from app.models.products import User
from app.models.products import Customer
from django.contrib import messages
from django.db.models import Q


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
class AuthenticateC:
	def valid_customer(function):
		def wrap(request):
			try:
				# User.objects.get(email=request.session['email'])
				Customer.objects.get(Q(password=request.session['password']) & Q(email=request.session['email']))
				return function (request)
			except:
				messages.warning(request,"Invalid email or password")
				return redirect('/login')
		return wrap
