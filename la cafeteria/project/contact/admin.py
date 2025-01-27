from django.contrib import admin
from . models import ContactModels
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','email')
    
admin.site.register(ContactModels,ContactAdmin)