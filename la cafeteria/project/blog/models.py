from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actializacion')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created']
        
    def __str__(self):
        return self.name

class BlogModels(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='blog', verbose_name='Imagen')
    date = models.DateTimeField(default=now, verbose_name='Fecha de creacion')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='autor')
    categorys = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_category')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
    
    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']
        
    def __str__(self):
        return self.title