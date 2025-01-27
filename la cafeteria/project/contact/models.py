from django.db import models
from django.utils.timezone import now
# Create your models here.
class ContactModels(models.Model):
    name = models.CharField(max_length=150, verbose_name='nombre')
    email = models.EmailField(verbose_name='correo')
    content = models.TextField(verbose_name='contenido')
    created = models.DateTimeField(default=now, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['name']
    
    def __str__(self):
        return self.name