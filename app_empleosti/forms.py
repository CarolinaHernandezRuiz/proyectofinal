from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
    class Meta: 
        model = Comentarios
        fields = ["nombre", "telefono", "email",  "comentario"]
    #fields = '__all__',

    #nombre = forms.CharField(widget=forms.TextInput(attrs= {'class':'contact-form contact-form-padding'}))
   #telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'contact-form contact-form-padding'}))
    #email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'contact-form contact-form-padding'}))
    #comentario = forms.CharField(widget=forms.TextInput(attrs={'class':'contact-form contact-form-padding'}))