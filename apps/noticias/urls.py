from django.urls import path
from . import views # Clase del 3-7-25
from django.conf.urls.static import static
from django.conf import settings

app_name = "noticias"

urlpatterns = [
  path('',views.Listar_Articulo, name = 'inicio'),
  path('Noticias/',views.Listar_Categoria, name= "path_listar_categorias"),
  path('Crear/',views.Crear_Articulo.as_view(),name = 'path_crear_articulo'),
  path('Listar', views.Listar_Articulo, name = "path_listar_noticias"),
  path('Detalle/<int:pk>', views.Detalle_Articulo.as_view(),name= "path_detalle_articulo"),
  path('Eliminar/<int:pk>',views.Borrar_Articulo.as_view(),name = 'path_borrar_articulo'),
  path('Modificar/<int:pk>',views.Modificar_Articulo.as_view(),name='path_modificar_articulo'),
  path('qom/', views.Filtro_QOM, name='filtro_qom'),
  path('wichi/', views.Filtro_WICHI, name='filtro_wichi'),
  path('mocovi/', views.Filtro_MOCOVI, name='filtro_mocovi'),
  path('buscar/', views.buscar_noticias, name='buscar'),
  path('Acerca/', views.Acerca_de, name='acerca_de'),  
  path('Contacto/', views.Contacto, name='contacto'),
      
]