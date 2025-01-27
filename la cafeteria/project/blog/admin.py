from django.contrib import admin
from .models import BlogModels, Category
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'date', 'get_list_category')
    date_hierarchy = 'date'
    list_filter = ('categorys', 'author__username')
    
    def get_list_category(self, obj):
        return ", ".join([c.name for c in obj.categorys.all().order_by('name')])
    get_list_category.short_description = 'categorias'
    
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created')
    
admin.site.register(BlogModels, BlogAdmin)
admin.site.register(Category, CategoryAdmin)