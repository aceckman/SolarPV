from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', views.ProductView)
router.register('certificate', views.CertificateView)
router.register('service', views.ServiceView)

urlpatterns = [
	path('', include(router.urls))
]