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
from django.conf.urls import url

from administrador.views import ReclamoListView, ReclamoDetailView

urlpatterns = [
#    url('accounts/', include('django.contrib.auth.urls')),
#
    url(r'^reclamos/$', ReclamoListView.as_view(), name='reclamos'),
    url(r'^editar-reclamo/(?P<pk>[0-9]+)$', ReclamoDetailView.as_view(), name='editar-reclamo'),
    url(r'^$', ReclamoListView.as_view(), name='reclamos'),

]