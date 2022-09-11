from django.shortcuts import render, redirect
from .models import Product, PlusCard
from .forms import ProductForm, CardForm
from django.http import HttpResponseRedirect



def MainPage(request):
	form =  ProductForm()
	cardForm = CardForm()
	if request.method == 'POST' and 'add_new_card' in request.POST:
		cardForm = CardForm(request.POST)
		if cardForm.is_valid():
			cardForm.save()
			return HttpResponseRedirect('/')
	if request.method == 'POST' and 'add_new_zam' in request.POST:
		form = ProductForm(request.POST)
		print('a')
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')


	name = Product.objects.all()
	return render(request,"MainPageR.html",{'form':form,'name':name,
											'cardForm':cardForm})

