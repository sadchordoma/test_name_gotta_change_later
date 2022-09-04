from django.contrib import admin
from .models import Product, PlusCard

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(Product, ProductAdmin)

class CardAdmin(admin.ModelAdmin):
	list_display = ['name']
admin.site.register(PlusCard, CardAdmin)