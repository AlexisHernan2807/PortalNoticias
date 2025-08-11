from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect
from .models import Comentario
from noticias.models import Articulo
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .forms import FormularioModificarComentario

def Comentar(request, pk):
	art = Articulo.objects.get(pk = pk)
	usuario = request.user
	com = request.POST.get('comentario',None)

	Comentario.objects.create(texto = com, articulo = art, usuario = usuario)

	return HttpResponseRedirect(reverse_lazy('noticias:path_detalle_articulo', kwargs={'pk':pk}))

class Eliminar(DeleteView):
	model = Comentario
	def get_success_url(self):
		return reverse_lazy('noticias:path_detalle_articulo', kwargs={'pk':self.object.articulo.pk})

class Modificar_Comentario(UpdateView):
	model = Comentario
	template_name = 'comentarios/modificar_comentario.html'
	form_class = FormularioModificarComentario
	def get_success_url(self):
		return reverse_lazy('noticias:path_detalle_articulo', kwargs={'pk':self.object.articulo.pk})
	

def Acerca_de(request):
    return render(request,'noticias/acerca_de.html')
	
	
