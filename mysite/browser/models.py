from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class categoria(models.Model):
	idCategoria = models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=60)
	descripcion= models.TextField()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nombre


# Create your models here.
