from perfil.models import Contacto
from django import forms

class ContactoForm(forms.ModelForm):
    """ProyectoForm definition."""
    nombre = forms.CharField(label="Titulo", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #Descripción del proyecto
    correo=forms.EmailField(label="Correo",widget=forms.TextInput(attrs={'class': 'form-control'}))
    #Tags: HTML, CSS, PYTHON, etc
    asunto = forms.CharField(label="Asunto",max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'class': 'form-control',"rows":"5"}))

    #Formulario con validación
    
    class Meta:
        model=Contacto
        fields=['nombre','correo','asunto','mensaje','user']