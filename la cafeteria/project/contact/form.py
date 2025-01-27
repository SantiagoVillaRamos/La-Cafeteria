from django import forms 

class ContactForms(forms.Form):
    name = forms.CharField(required=True, label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    email = forms.EmailField(required=True, label='Email', max_length=150, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Correo'}))
    content = forms.CharField(required=True, label='Contenido', max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Contenido', 'rows':3}))
    