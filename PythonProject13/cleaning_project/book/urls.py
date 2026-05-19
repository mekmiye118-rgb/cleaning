from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('succe/', views.succe, name='succe'), # URL name used in redirect('success')
    path('dach/', views.dach, name='dach'),
]