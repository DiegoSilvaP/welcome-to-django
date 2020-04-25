from django.db import models

# Create your models here.
class Historia(models.Model):
    title = models.CharField(max_length=64, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")

    class Meta:
        verbose_name_plural="Historia"

    def __str__(self):
        return self.title