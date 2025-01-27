from django.shortcuts import render, redirect
from django.urls import reverse
from . form import ContactForms
from .models import ContactModels
# Create your views here.
def contact(request):
    
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            
            models = ContactModels(name=name, email=email, content=content)
            models.save()
            
            return redirect(reverse('contact')+'?ok')
        
    else:
        form = ContactForms()
    
    return render(request, 'core/contact.html', {'forms':form})
