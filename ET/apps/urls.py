from django.urls import path,include
from .views import paginaprincipal


urlpatterns = [
    path('',paginaprincipal,name='paginaprincipal')
]