from django import forms
from .models import Product, PlusCard

class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ['name']

		widgets = {
			"name": forms.TextInput(),
		}

class CardForm(forms.ModelForm):

	class Meta:
		model = PlusCard
		fields = ['name']

		widgets = {
			"name": forms.TextInput(),
		}