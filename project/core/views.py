from django.shortcuts import render

# Create your views here.
from . import models
def inicio(request):
    return render(request, "core/index.html")
