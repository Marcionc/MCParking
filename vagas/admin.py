from django.contrib import admin
from .models import Vagas

class VagasAdmin(admin.ModelAdmin):
    list_display = ['placa', 'nome', 'date_in', 'date_pay', 'date_out',  'value']


admin.site.register(Vagas, VagasAdmin)
