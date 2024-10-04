from .views import index,create_tenant
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('create_tenant',create_tenant)
]