# -*- coding: utf-8 -*-
# Create your views here.
from rest_framework import permissions
from rest_framework import viewsets

from api.models import Categoria, Subcategoria, Reclamo
from api.serializers import CategoriaSerializer, SubcategoriaSerializer, ReclamoSerializer
from rest_framework.response import Response
from rest_framework import status


from rest_framework import serializers

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubcategoriaViewSet(viewsets.ModelViewSet):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReclamoViewSet(viewsets.ModelViewSet):
    queryset = Reclamo.objects.all()
    serializer_class = ReclamoSerializer
    permission_classes = [permissions.IsAuthenticated]

    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset=queryset.filter(usuario=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.usuario!=request.user:
            raise serializers.ValidationError({'non_field_error': [u"Unauthorized"]})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

