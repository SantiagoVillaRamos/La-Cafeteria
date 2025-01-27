from django.contrib import admin
from .models import ServicesModels
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title', 'created')
    
    
admin.site.register(ServicesModels, ServicesAdmin)