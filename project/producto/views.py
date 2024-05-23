from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render,  redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import forms,models

from . import models
def inicio(request):

    return render(request, "producto/index.html")

def productocategoria_list(request):
    consulta = request.GET.get("consulta") 
    if consulta:
        print (consulta)
        query = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
    else:
        query = models.ProductoCategoria.objects.all()

    context = {"productos": query}
    return render(request, "producto/index.html")

def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:inicio")
    else:
        form = forms.ProductoCategoriaForm()
        return render(request, "producto/productocategoria_create.html",context={"form": form})

def productocategoria_detail(request,pk):
    query = models.ProductoCategoria.objets.get(id=pk)
    return render(request, "producto/productocategoria_detail.html", {"producto":query})

def productocategoria_update(request, pk):
    query= models.ProductoCategoria.objets.get(id=pk)
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("producto:productocategoria_list")
    else:
        form = forms.ProductoCategoriaForm(instance=query)
    return render(request, "producto/productocategoria_update.html",context={"form": form})

def productocategoria_delete(request, pk):
    query= models.ProductoCategoria.objets.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("producto:productocategoria_list")
    return render(request, "producto/productocategoria_delete.html",context={"producto": query})



