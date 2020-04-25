from django.db import models

# Create your models here.

# Nos sirve para sustituir la imagen cada vez que se actualiza la portada, así no se almacenan
def portada_custom_upload_to(instance, filename):
    if instance.pk == None:
        print("pk",instance.pk)
        return 'portada/'+filename
    else:
        old_instance =Portada.objects.get(pk=instance.pk)
        print("old_instance",old_instance)
        old_instance.image.delete()
        return 'portada/'+filename

# El nombre de los modelos va con CamelCase y singular
# Las propiedades va en minúscula y con guion bajo: link_text
class Portada(models.Model):
    image = models.ImageField(upload_to=portada_custom_upload_to, verbose_name="Imagen")
    title = models.CharField(max_length=150, verbose_name="Título")
    subtitle = models.CharField(max_length=150, verbose_name="Subtítulo")
    link = models.URLField(blank=True, verbose_name="Link de la portada")
    link_text = models.CharField(max_length=16, verbose_name="Texto del botón")

    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name='Inicio'
        verbose_name_plural = 'Inicio'
        # por defecto, django ordena del más viejo al mas nuevo, por lo que se le agrega un - para ordenar del mas nuevo al mas viejo
        ordering = ['-created']

    def __str__(self):
        return self.title


def noticias_custom_upload_to(instance, filename):
    if instance.pk == None:
        return 'noticias/'+filename
    else:
        old_instance = Noticia.objects.get(pk=instance.pk)
        old_instance.image.delete()
        return 'noticias/'+filename

class Noticia(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    subtitle = models.CharField(max_length=150, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to=noticias_custom_upload_to, verbose_name="Imagen")
    home = models.ForeignKey(Portada, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title


VERTICAL_CHOICES = (
    ('top', 'Top'),
    ('bottom', 'Bottom'),
)
HORIZONTAL_CHOICES = (
    ('right', 'Right'),
    ('left', 'Left'),
)
SIZE_OPTIONS = (
    (10,10),
    (20,20),
    (30,30),
    (50,50),
)


def bot_custom_upload_to(instance, filename):
    if instance.pk == None:
        return 'bot/'+filename
    else:
        old_instance = BotAplication.objects.get(pk=instance.pk)
        old_instance.button_icon.delete()
        return 'bot/'+filename

class BotAplication(models.Model):
    name = models.CharField(max_length=160, default="Bot App", verbose_name="Nombre")
    endpoint = models.URLField(max_length=200, null=True, blank=True, verbose_name="URL del bot", help_text="Coloca sólo el endpoint")
    vertical_position = models.CharField(choices=VERTICAL_CHOICES, default='bottom', max_length=15, verbose_name="Posición vertical")
    horizontal_position = models.CharField(choices=HORIZONTAL_CHOICES, default='right', max_length=15, verbose_name="Posición Horizontal")
    button_icon = models.ImageField(upload_to=bot_custom_upload_to,verbose_name="Ícono", help_text="Formatos ico, jpg, png o gif. Relación de aspecto 1:1")
    button_size = models.IntegerField(choices=SIZE_OPTIONS, default=20, verbose_name="Tamaño del ícono")
    width = models.IntegerField(default=350, verbose_name="Ancho")
    height = models.IntegerField(default=500, verbose_name="Alto")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Bot'
        verbose_name_plural='Bot'

    def __str__(self):
        return self.name
