from django.contrib import admin

# Register your models here.
from api.models import Categoria, Subcategoria, Reclamo


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'organizacion',)
    list_filter = ('organizacion',)

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria','organizacion',)
    list_filter = ('categoria','organizacion', )


class ReclamoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', 'categoria', 'subcategoria', 'organizacion',)
    list_filter = ('organizacion', 'estado')

    def categoria(self, obj):
        return obj.subcategoria.categoria

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Reclamo, ReclamoAdmin)