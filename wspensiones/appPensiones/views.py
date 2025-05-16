from django.shortcuts import render, redirect
from .models import Pensionado

def index(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        edad = int(request.POST.get("edad"))
        edadRetiro = int(request.POST.get("edadretiro"))
        saldo = float(request.POST.get("saldo"))
        ahorro = float(request.POST.get("ahorro"))
        genero = request.POST.get("genero") == "on"

        pensionado = Pensionado(
            nombre=nombre,
            edad=edad,
            edadRetiro=edadRetiro,
            saldo=saldo,
            ahorro=ahorro,
            genero=genero
        )
        pensionado.save()

        return redirect('appPensionados:resultado', pensionado.id)

    return render(request, "appPensiones/index.html")



def resultado(request, pensionado_id):
    pensionado = Pensionado.objects.get(pk=pensionado_id)
    pension = pensionado.calcula_pension()
    return render(request, "appPensiones/resultado.html", {
        "pensionado": pensionado,
        "pension": pension
    })

def listar_pensionados(request):
    # Obtiene el criterio de ordenamiento de la URL (?orden=campo)
    orden = request.GET.get("orden", "nombre")
    # Para evitar inyecciones, limita a los campos válidos:
    campos_validos = ["nombre", "edad", "saldo", "ahorro"]
    if orden not in campos_validos:
        orden = "nombre"
    # Ordena
    pensionados = Pensionado.objects.all().order_by(orden)
    # Pasa el campo actual de orden al template
    return render(request, "appPensiones/listado.html", {
        "pensionados": pensionados,
        "orden": orden
    })