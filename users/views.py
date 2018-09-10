from django.conf import settings
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login as login_
from django.shortcuts import render, redirect
from users.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):

    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


class UsuarioList(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwords = request.POST.get('password')
        user = authenticate(username=username, password=passwords)

        next = request.POST.get('next')

        if user:
            login_(request, user)
            redirect_to = settings.LOGIN_REDIRECT_URL
            if next and next != '':
                redirect_to = next

            return redirect(redirect_to)

    return render(request, 'accounts/login.html')