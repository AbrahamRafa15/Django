from django.contrib import admin
from .models import Pensionado

@admin.register(Pensionado)
class PensionadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'edadRetiro', 'saldo', 'ahorro', 'genero']
    search_fields = ['nombre']
    list_filter = ['edadRetiro', 'genero']
    ordering = ['nombre']