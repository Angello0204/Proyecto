from django.shortcuts import render

# Create your views here.
from . import models
def inicio(request):
    consulta_de_productos = models. ProductoCategoria.objects.all()
    context={"productos": consulta_de_productos}
    return render(request, "producto/index.html", context)
