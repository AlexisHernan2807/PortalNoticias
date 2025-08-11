from django.contrib import admin

from .models import Articulo
from .models import Categoria

admin.site.register(Articulo)

admin.site.register(Categoria)
