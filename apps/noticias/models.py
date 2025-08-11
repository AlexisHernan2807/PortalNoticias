from django.db import models
from django.utils import timezone

# Modelo para las Categorías (ej: Qom, Wichi, Moqoit, etc.)
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    imagen = models.ImageField(upload_to='categorias',null= True)

    def __str__(self):
          return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    autor = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='articulos')
    # Nuevo campo para la imagen
    imagen = models.ImageField(upload_to='articulos', blank=True, null=True)
    # upload_to='noticias_imagenes/': Las imágenes se guardarán en MEDIA_ROOT/noticias_imagenes/
    # blank=True, null=True: Hace que el campo sea opcional

    
    def __str__(self):
        return self.titulo
    
    def misComentarios(self):
        return self.comentario_set.all()