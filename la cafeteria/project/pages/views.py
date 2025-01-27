from django.shortcuts import render,get_object_or_404
from .models import PagesModels
# Create your views here.
def page(request, page_id):
    models = get_object_or_404(PagesModels, id=page_id)
    return render(request, 'core/page.html', {'models':models})

