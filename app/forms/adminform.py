from django import forms
from app.models.products import User

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields="__all__"
