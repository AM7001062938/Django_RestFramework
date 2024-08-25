from django.contrib import admin
from django.urls import path, include
from mochi.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mochi.urls')),
    path('', home_view, name='home'),
]
