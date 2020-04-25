from django.db import models

# Create your models here.
class Caracteristica(models.Model):
    name = models.CharField(max_length=32, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
         ordering = ['-created']

    def __str__(self):
        return self.name