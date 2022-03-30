from urllib import request
from django.shortcuts import render
from .models import Empleo
from .forms import ComentariosForm

# Create your views here.
def index(request):
    emple = Empleo.objects.all()
    datos = {
        "Empleos" : emple
    }
    return render(request, 'app/index.html', datos)

def about(request):
    return render(request, 'app/about-us.html')

def services(request):
    return render(request, 'app/services.html')

def tabsaccordions(request):
    return render(request, 'app/tabs-and-accordions.html')

def news(request):
    return render(request, 'app/news.html')


def contact(request):
    datos ={
        "form": ComentariosForm
    }
    if request.method == 'POST':
        formulario = ComentariosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datos["form"] = formulario
    return render(request, 'app/contact-us.html',datos)


def newspost(request):
    return render(request, 'app/news-post.html')

def single(request):
    return render(request, 'app/single-services.html')

def Terminos(request):
    return render(request, 'app/terms-and-conditions.html')


def Privacidad(request):
    return render(request, 'app/privacy-policy.html')

def buscar(request):
    if request.GET['busqueda']:
        query = request.GET['busqueda']
        empleos = Empleo.objects.filter(titulo__icontains=query).order_by('category')
        datos = {
            "Empleos": empleos,
            "query": query
        }
        return render(request, 'app/buscar.html', datos)
    else:
        return render(request, 'app/buscar.html')
