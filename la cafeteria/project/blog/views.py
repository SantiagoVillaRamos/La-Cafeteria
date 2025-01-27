from django.shortcuts import render,get_object_or_404
from .models import BlogModels, Category
# Create your views here.
def blog(request):
    post = BlogModels.objects.all()
    return render(request, 'core/blog.html', {'posts':post})

def category(request, category_id):
    categorys = get_object_or_404(Category, id=category_id)
    return render(request, 'core/category.html', {'categorys':categorys})