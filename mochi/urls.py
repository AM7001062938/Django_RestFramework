from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, register_create_view

router = DefaultRouter()
router.register(r'registers', RegisterViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/create/', register_create_view, name='register_create'),
    path('', include(router.urls)),
]
