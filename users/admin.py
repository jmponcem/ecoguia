from django.contrib import admin
from .models import Consulta

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'confirmarcorreo', 'rut', 'telefono', 'asunto', 'mensaje')


admin.site.register(Consulta, ConsultaAdmin)


