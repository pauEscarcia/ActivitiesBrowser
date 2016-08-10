from django.contrib import admin
from .models import categoria, clasificacion, actividad, prestador, actividadPrestador

# Register your models here.
admin.site.register(categoria)
admin.site.register(clasificacion)
admin.site.register(actividad)
admin.site.register(prestador)
admin.site.register(actividadPrestador)