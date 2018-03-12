"""reclamos_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from api.views import CategoriaList, CategoriaDetail, SubcategoriaList, SubcategoriaDetail, ReclamoDetail, ReclamoList
from users.views import UsuarioList

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^usuario/$', UsuarioList.as_view()),
    url(r'^categoria/$', CategoriaList.as_view()),
    url(r'^categoria/(?P<pk>[0-9]+)/$', CategoriaDetail.as_view()),
    url(r'^subcategoria/categoria/(?P<pk>[0-9]+)/$', SubcategoriaList.as_view()),
    url(r'^subcategoria/(?P<pk>[0-9]+)/$', SubcategoriaDetail.as_view()),
    url(r'^reclamo/$', ReclamoList.as_view()),
    url(r'^reclamo/(?P<pk>[0-9]+)/$', ReclamoDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)