from pyexpat import model
from django import forms
from .models import Comentarios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ComentariosForm(forms.ModelForm):
    class Meta: 
        model = Comentarios
        fields = ["nombre", "telefono", "email",  "comentario"]
    #fields = '__all__',

class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']

class loginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'contact-form contact-form-padding',}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'contact-form contact-form-padding', 'data-toggle': 'password', 'id': 'password', 'name': 'password',}))
    remember_me = forms.BooleanField(required=False)
    
    #nombre = forms.CharField(widget=forms.TextInput(attrs= {'class':'contact-form contact-form-padding'}))
    #telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'contact-form contact-form-padding'}))
    #email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'contact-form contact-form-padding'}))
    #comentario = forms.CharField(widget=forms.TextInput(attrs={'class':'contact-form contact-form-padding'}))