from django.shortcuts import render
from . models import ServicesModels
# Create your views here.
def services(request):
    models = ServicesModels.objects.all()
    return render(request, 'core/services.html', {'models':models})