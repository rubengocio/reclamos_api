from django.contrib import admin

# Register your models here.
from api.models import Categoria, Subcategoria, Reclamo

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
    list_filter = ('categoria', )


admin.site.register(Categoria)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Reclamo)