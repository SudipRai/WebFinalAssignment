from django.db import models

# Create your models here.
class Product(models.Model):
	id:models.AutoField(auto_created=True,primary_key=True)
	name=models.CharField(max_length=100)
	price=models.IntegerField(max_length=100)
	category=models.CharField(max_length=100)
	image=models.ImageField(default="img.jpg")
	class Meta:
		db_table="product"




class Customer(models.Model):
	id:models.AutoField(auto_created=True,primary_key=True)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	city=models.CharField(max_length=200)
	state=models.CharField(max_length=200)
	zipcode=models.CharField(max_length=200)
	class Meta:
		db_table="customer"

class User(models.Model):
	id:models.AutoField(auto_created=True,primary_key=True)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	image=models.ImageField(default="img.jpg")
	class Meta:
		db_table="user"


class Order(models.Model):
	orderid=models.AutoField(auto_created=True,primary_key=True)
	productid=models.ForeignKey(Product,on_delete=models.CASCADE)
	customername=models.CharField(max_length=100)
	quantity=models.CharField(max_length=50)
	orderdate=models.CharField(max_length=50)
	class Meta:
		db_table="order"
