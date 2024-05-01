from django.db import models

# Create your models here.
class ProductoCategoria (models.Model):
    '''Categoria de productos'''
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name ='descripcion')

    def __str__(self) -> str:
        return self.nombre
    
 

    class Meta:
        verbose_name = "categoría de productos"
        verbose_name_plural = "categorías de productos"
