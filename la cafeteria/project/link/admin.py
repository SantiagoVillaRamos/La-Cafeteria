from django.contrib import admin
from . models import LinksModels
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields =('created', 'updated')
    list_display = ('name', 'created')
    
admin.site.register(LinksModels, LinkAdmin)