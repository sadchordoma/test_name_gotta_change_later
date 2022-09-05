from django.shortcuts import render, redirect
from .models import Product, PlusCard
from .forms import ProductForm, CardForm
from django.http import HttpResponseRedirect



def MainPage(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	form =  ProductForm()
	FormCard = PlusCard.objects.all()
	name = Product.objects.all()
	return render(request,"MainRavil.html",{'form':form,'name':name,'card':FormCard})

