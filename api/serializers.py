from django.contrib.auth.models import User
from rest_framework import serializers

from api.fields import Base64ImageField
from api.models import Categoria, Subcategoria, Reclamo


class SubcategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategoria
        fields = (
            'id',
            'nombre',
            'imagen'
        )


class CategoriaSerializer(serializers.ModelSerializer):
    subcategorias = serializers.SerializerMethodField()

    class Meta:
        model = Categoria
        fields = (
            'id',
            'nombre',
            'imagen',
            'subcategorias'
        )

    def get_subcategorias(self, obj):
        resutl = Subcategoria.objects.filter(categoria=obj)
        serializer = SubcategoriaSerializer(resutl, many=True, context=self.context)
        return serializer.data


class SubcategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategoria
        fields = (
            'id',
            'nombre',
            'imagen'
        )


class CategoriaReclamoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = (
            'id',
            'nombre'
        )


class SubcategoriaReclamoSerializer(serializers.ModelSerializer):
    categoria = CategoriaReclamoSerializer(required=False)

    class Meta:
        model = Subcategoria
        fields = (
            'id',
            'nombre',
            'categoria'
        )


class ReclamoSerializer(serializers.ModelSerializer):
    subcategoria = SubcategoriaReclamoSerializer(many=False)
    imagen = Base64ImageField(required=False)
    usuario = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Reclamo
        fields = (
            'id',
            'subcategoria',
            'imagen',
            'descripcion',
            'calle',
            'numero',
            'coord_x',
            'coord_y',
            'usuario',
            'estado',
            'created_at',
            'updated_at'
        )


    def create(self, validated_data):

        id = self.initial_data['subcategoria']['id']
        #usuario_id = self.initial_data['usuario']['id']
        validated_data['subcategoria'] = Subcategoria.objects.get(id=id)
        #validated_data['usuario'] = User.objects.get(pk=usuario_id)

        return Reclamo.objects.create(**validated_data)