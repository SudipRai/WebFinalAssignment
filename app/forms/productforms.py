from django import forms
from app.models.models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields="__all__"