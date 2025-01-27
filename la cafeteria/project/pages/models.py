from django.db import models

# Create your models here.
class PagesModels(models.Model):
    title = models.CharField(max_length=100, verbose_name='TItulo')
    content = models.TextField(verbose_name='Contenido')
    order = models.SmallIntegerField(default=0, verbose_name='Orden')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fechas de actualizacion')
    
    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas genericas'
        ordering = ['order', 'title']
        
    def __str__(self):
        return self.title