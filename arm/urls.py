from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('up/', views.up, name='up'),
    path('down/', views.down, name='down'),
]