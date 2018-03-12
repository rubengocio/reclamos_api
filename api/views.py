import hashlib

from django.http import Http404
from django.shortcuts import render
import base64

# Create your views here.
from rest_framework.views import APIView

from api.models import Categoria, Subcategoria, Reclamo
from api.serializers import CategoriaSerializer, SubcategoriaSerializer, ReclamoSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.files.base import ContentFile

class CategoriaList(APIView):

    def get(self, request, format=None):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaDetail(APIView):

    def get_object(self, pk):
        try:
            return Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        categoria = self.get_object(pk)
        categoria = CategoriaSerializer(categoria)
        return Response(categoria.data)

    def put(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubcategoriaList(APIView):

    def get(self, request, pk, format=None):
        subcategorias = Subcategoria.objects.filter(categoria__pk=pk)
        serializer = SubcategoriaSerializer(subcategorias, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubcategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubcategoriaDetail(APIView):

    def get_object(self, pk):
        try:
            return Subcategoria.objects.get(pk=pk)
        except Subcategoria.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        subcategoria = self.get_object(pk)
        subcategoria = SubcategoriaSerializer(subcategoria)
        return Response(subcategoria.data)

    def put(self, request, pk, format=None):
        subcategoria = self.get_object(pk)
        serializer = SubcategoriaSerializer(subcategoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReclamoList(APIView):

    def get(self, request, format=None):
        reclamos = Reclamo.objects.filter(usuario=request.user)
        serializer = ReclamoSerializer(reclamos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReclamoSerializer(data=request.data)
        imgstr64 = serializer.initial_data.get('imagen', None)

        if imgstr64:
            format, imgstr = imgstr64.split(';base64,')
            ext = format.split('/')[-1]
            hash = hashlib.sha1().hexdigest()
            data = ContentFile(base64.b64decode(imgstr), name=hash + '.' + ext)
            serializer.initial_data['imagen'] = data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReclamoDetail(APIView):

    def get_object(self, pk):
        try:
            return Reclamo.objects.get(pk=pk)
        except Subcategoria.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reclamo = self.get_object(pk)
        reclamo = ReclamoSerializer(reclamo)
        return Response(reclamo.data)

    def put(self, request, pk, format=None):
        reclamo = self.get_object(pk)
        serializer = ReclamoSerializer(reclamo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reclamo = self.get_object(pk)
        reclamo.delete()
        return Response({ 'ok': True } ,status=status.HTTP_201_CREATED)

