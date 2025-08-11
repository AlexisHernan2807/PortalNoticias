from django.shortcuts import render,get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .forms import FormularioCrearArticulo,FormularioModificarArticulo

from .models import Categoria
from .models import Articulo
#DECORADOR PARA UNA VBF QUE CONTROLA SI EL USUARIO ESTA LOGUEADO
from django.contrib.auth.decorators import login_required

#MIXINS PARA UNA VBC QUE CONTROLA SI EL USUARIO ESTA LOGUEADO
from django.contrib.auth.mixins import LoginRequiredMixin


def Listar_Categoria(request):
    categorias = Categoria.objects.all()
    return render(request,'noticias/categoria.html',{'categorias':categorias})

class Crear_Articulo(LoginRequiredMixin,CreateView):
	model = Articulo
	template_name = 'noticias/crear_articulo.html'
	form_class = FormularioCrearArticulo
	success_url = reverse_lazy('noticias:inicio')
	#una vez que se creo correctamente a ke pagina me redirecciona,en este caso a la lista de productos.

def Listar_Articulo(request):
    articulos = Articulo.objects.all()
    orden = request.GET.get('orden', None)
    
    if orden:
        if orden == 'asc':
            articulos = articulos.order_by('fecha_publicacion')
        else:
            articulos = articulos.order_by('-fecha_publicacion')

    return render(request,'noticias/listar_articulo.html',{'articulo':articulos})

         
class Detalle_Articulo(DetailView):
	template_name = 'noticias/detalle_articulo.html'
	model = Articulo
	context_object_name = 'articulo'
      
class Borrar_Articulo(DeleteView):
	model = Articulo
	success_url = reverse_lazy('noticias:path_listar_noticias')
	
class Modificar_Articulo(UpdateView):
	model = Articulo
	template_name = 'noticias/modificar_articulo.html'
	form_class = FormularioModificarArticulo
	success_url = reverse_lazy('noticias:path_listar_noticias')	

def Filtro_QOM(request):
    qom_categoria = get_object_or_404(Categoria, pk=1)
    articulos_qom = Articulo.objects.filter(categoria=qom_categoria).order_by('-fecha_publicacion')
    orden = request.GET.get('orden')
    if orden == 'asc':
        articulos_qom = articulos_qom.order_by('fecha_publicacion')
    contexto = {
        'categoria': qom_categoria,
        'articulos': articulos_qom,
    }
    return render(request, 'noticias/filtro_qom.html', contexto)

def Filtro_WICHI(request):
    wichi_categoria = get_object_or_404(Categoria, pk=2)
    articulos_wichi = Articulo.objects.filter(categoria=wichi_categoria).order_by('-fecha_publicacion')
    orden = request.GET.get('orden')
    if orden == 'asc':
        articulos_wichi = articulos_wichi.order_by('fecha_publicacion')
    contexto = {
        'categoria': wichi_categoria,
        'articulos': articulos_wichi,
    }
    return render(request, 'noticias/filtro_wichi.html', contexto)

def Filtro_MOCOVI(request):
    mocovi_categoria = get_object_or_404(Categoria, pk=3)
    articulos_mocovi = Articulo.objects.filter(categoria=mocovi_categoria).order_by('-fecha_publicacion')
    orden = request.GET.get('orden')
    if orden == 'asc':
        articulos_mocovi = articulos_mocovi.order_by('fecha_publicacion')
    contexto = {
        'categoria': mocovi_categoria,
        'articulos': articulos_mocovi,
    }
    return render(request, 'noticias/filtro_mocovi.html', contexto)

def Ordenar_Noticias(request):
    articulos = Articulo.objects.all()
    orden = request.GET.get('orden', None)
    
    if orden:
        if orden == 'asc':
              articulos = articulos.order_by('fecha_publicacion')

        else :
             articulos = articulos.order_by('-fecha_publicacion')
       
    categorias = Categoria.objects.all()
    return render(request, 'noticias/ordenar_noticias.html', {'articulos': articulos, 'noticias': categorias})

def buscar_noticias(request):
    query = request.GET.get('q')
    if query:
        resultados = Articulo.objects.filter(titulo__icontains=query)
    else:
        resultados = Articulo.objects.all()

    return render(request, 'noticias/resultados_busqueda.html', {'resultados': resultados, 'query': query})

def Acerca_de(request):
    return render(request,'noticias/acerca_de.html')


def Contacto(request):
    return render(request,'noticias/contacto.html')