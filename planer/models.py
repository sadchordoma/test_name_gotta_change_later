from django.db import models


class Product(models.Model):


	name = models.CharField(max_length=200, db_index=True) # Имя

	def __str__(self):
		return self.name
