from django.contrib import admin
from django.urls import path,include
from . import views 
# Importa estas dos para servir archivos de medios en desarrollo
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.home, name='path_home'),  # Ruta para la vista de inicio clase del 3-7-25

    #path('Nosotros/',views.nosotros, name= 'nosotros'),
    path('', include('noticias.urls')),
    path('Usuarios/',include('usuarios.urls')),
    path('Comentarios/',include('comentarios.urls')),
    
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

