from django.conf.urls import url
from rest_framework import routers
from api.views import CategoriaViewSet, SubcategoriaViewSet, ReclamoViewSet

router = routers.DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'subcategoria', SubcategoriaViewSet)
router.register(r'reclamo', ReclamoViewSet)

urlpatterns = router.urls

