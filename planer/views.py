from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def MainPage(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
	form =  ProductForm()
	name = Product.objects.all()
	return render(request,"MainPage.html",{'form':form,'name':name})