from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('baseclockwise/', views.baseclockwise, name='baseclockwise'),
    path('baseanticlockwise/', views.baseanticlockwise, name='baseanticlockwise'),
    path('up/', views.up, name='up'),
    path('down/', views.down, name='down'),
    path('elbowup/', views.elbowup, name='elbowup'),
    path('elbowdown/', views.elbowdown, name='elbowdown'),
    path('wristup/', views.wristup, name='wristup'),
    path('wristdown/', views.wristdown, name='wristdown'),
    path('gripopen/', views.gripopen, name='gripopen'),
    path('gripclose/', views.gripclose, name='gripclose'),
    path('lighton/', views.lighton, name='lighton'),
    path('lightoff/', views.lightoff, name='lightoff'),
]