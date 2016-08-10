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

class clasificacion (models.Model):
	idClasificacion = models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=60)
	descripcion= models.TextField()
	categoria_idCategoria = models.ForeignKey('categoria')
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nombre
class actividad (models.Model):
	idActividad = models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=60)
	descripcion= models.TextField()
	disponibilidad= models.CharField(max_length=60)
	duracion= models.CharField(max_length=60)
	clasificacion_idClasificacion = models.ForeignKey('clasificacion')
	costo= models.TextField()
	divisa= models.CharField(max_length=60)
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nombre
class prestador (models.Model):
	idprestador = models.AutoField(primary_key=True)
	fecha = models.DateTimeField(default=timezone.now)
	nomOrganizacion= models.CharField(max_length=60)
	direccion= models.CharField(max_length=60)
	gerente= models.CharField(max_length=60)
	emaii= models.EmailField()
	pagina= models.URLField()
	facebook= models.CharField(max_length=60, blank=True)
	youtube= models.CharField(max_length=60, blank=True)
	whatsapp= models.CharField(max_length=60, blank=True)
	instagram= models.CharField(max_length=60, blank=True)
	twitter= models.CharField(max_length=60, blank=True)
	tumblr= models.CharField(max_length=60, blank=True)
	telEmpresa= models.CharField(max_length=60)
	telCel= models.CharField(max_length=60, blank=True)
	latitud=models.TextField()
	longitud=models.TextField()
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nomOrganizacion

class actividadPrestador (models.Model):
	idActividadPrestador = models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=60)
	actividad_idActividad = models.ForeignKey('actividad')
	categoria_idPrestador = models.ForeignKey('prestador')
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.nombre








# Create your models here.
