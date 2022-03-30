from django.urls import path
from .views import about, index, services, tabsaccordions, news, contact, newspost, single, Terminos, Privacidad, buscar
from django.conf.urls.static import static
from django.conf import settings

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
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)