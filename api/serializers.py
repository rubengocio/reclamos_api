from django.conf.global_settings import MEDIA_ROOT
from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Categoria, Subcategoria, Reclamo


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'


class SubcategoriaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(many=False)

    class Meta:
        model = Subcategoria
        fields = '__all__'


class ReclamoSerializer(serializers.ModelSerializer):
    subcategoria = SubcategoriaSerializer(many=False)

    class Meta:
        model = Reclamo
        fields = ('__all__')
        depth = 1

    def create(self, validated_data):

        id = self.initial_data['subcategoria']['id']
        usuario_id = self.initial_data['usuario']['id']
        validated_data['subcategoria'] = Subcategoria.objects.get(id=id)
        validated_data['usuario'] = User.objects.get(pk=usuario_id)

        return Reclamo.objects.create(**validated_data)