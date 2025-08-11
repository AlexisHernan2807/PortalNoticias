from django import forms
from .models import Comentario

class FormularioModificarComentario(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('texto',)