from unicodedata import name
from django.shortcuts import redirect
from django.urls import path
from .views import CustomLoginView, Registro, about, index, services, tabsaccordions, news, contact, newspost, single, Terminos, Privacidad, buscar, Registro, CustomLoginView
from django.conf.urls.static import static
from django.conf import settings
from .forms import loginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='Inicio'),
    path('about/', about, name='SobreNosotros'),
    path('services/', services, name='Servicios'),
    path('tabsaccordions/', tabsaccordions, name='PestañasyAcordes'),
    path('news/', news, name='Noticias'),
    path('contact-us/', contact, name='Contactanos'),
    path('news-post/', newspost, name='NoticiasPublicadas'),
    path('single-services/', single, name='Soluciones'),
    path('terms-conditions/', Terminos, name='Terminos'),
    path('privacy-policy/', Privacidad, name='Privacidad'),
    path('buscar/', buscar, name='buscar'),
    path('registro/', Registro.as_view(), name='registro'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='app/login.html', authentication_form=loginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'app/logout.html'), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)