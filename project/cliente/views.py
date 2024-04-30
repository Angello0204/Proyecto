from django.shortcuts import render

# Create your views here.
from . import models
def inicio(request):
    consulta_de_clientes = models.Cliente.objects.all()
    context={"clientes": consulta_de_clientes}
    return render(request, "cliente/index.html", context)
