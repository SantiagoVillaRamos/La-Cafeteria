from django.db import models

# Create your models here.
class LinksModels(models.Model):
    key = models.SlugField(unique=True, verbose_name='Clave')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    link = models.URLField(null=True, blank=True, verbose_name='Link')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
    
    class Meta:
        verbose_name = 'red social'
        verbose_name_plural = 'redes sociales'
        ordering = ['name']
        
    def __str__(self):
        return self.name    