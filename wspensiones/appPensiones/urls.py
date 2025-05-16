from django.urls import path
from . import views

app_name = "appPensionados"

urlpatterns = [
    
    path("", views.index,name="index"),
    path("resultado/<int:pensionado_id>/", views.resultado, name="resultado"),
    path("listado/", views.listar_pensionados, name="listado"),
]