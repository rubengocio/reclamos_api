from _datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from users.models import Organization


class Categoria(models.Model):
    nombre = models.CharField(max_length=256)
    imagen = models.CharField(max_length=256,blank=True, null=True)
    organizacion=models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class Subcategoria(models.Model):
    nombre = models.CharField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True, related_name='categoria')
    imagen = models.CharField(max_length=256, blank=True, null=True)
    organizacion = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return u'%s - %s' % (self.categoria.nombre, self.nombre)

    def __unicode__(self):
        return u'%s - %s' % (self.categoria.nombre, self.nombre)


class Reclamo(models.Model):
    NUEVO = 1
    EN_PROGRESO = 2
    FINALIZADO = 3
    CANCELADO = 4

    ESTADOS_PEDIDO_CHOICES = (
        (NUEVO, u'Nuevo'),
        (EN_PROGRESO, u'En Progreso'),
        (FINALIZADO, u'Finalizado'),
        (CANCELADO, u'Cancelado')
    )

    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.SET_NULL, blank=True, null=True, related_name='subcategoria')
    imagen = models.ImageField(upload_to="relamos/images/", null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    calle = models.CharField(max_length=256, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    coord_x = models.FloatField(blank=True, null=True)
    coord_y = models.FloatField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    estado = models.IntegerField(choices=ESTADOS_PEDIDO_CHOICES, default=NUEVO, null=True)
    organizacion = models.ForeignKey(Organization, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=datetime.now())
    updated_at = models.DateTimeField(auto_now=datetime.now())

    def __str__(self):
        return self.subcategoria.nombre if self.subcategoria else ''

    def __unicode__(self):
        return self.subcategoria.nombre if self.subcategoria else ''

    @property
    def get_estado(self):
        for tuple in Reclamo.ESTADOS_PEDIDO_CHOICES:
            if tuple[0] == self.estado:
                return tuple[1]
        return None

