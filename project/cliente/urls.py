from django.urls import path

app_name= "cliente"

from . import views

urlpatterns = [
    path("",views.inicio , name='inicio'), 
]