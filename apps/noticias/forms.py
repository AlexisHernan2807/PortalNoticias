from django import forms
from .models import Articulo



class FormularioCrearArticulo(forms.ModelForm):

	class Meta:
		model = Articulo
		fields = ('titulo','contenido','categoria','imagen') 

class FormularioModificarArticulo(forms.ModelForm):

	class Meta:
		model = Articulo
		fields = ('titulo','contenido','imagen','categoria')
