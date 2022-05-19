from django.contrib import admin
from .models import Veiculos

class VeiculosAdmin(admin.ModelAdmin):
    list_display = ['placa', 'marca', 'modelo', 'cor', 'is_ativo',  'is_especial', 'is_plan']

admin.site.register(Veiculos, VeiculosAdmin)