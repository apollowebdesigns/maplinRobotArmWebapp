from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stop/', views.stop, name='stop'),
    path('left/', views.left, name='left'),
    path('right/', views.right, name='right'),
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
    path('backwards/', views.backwards, name='backwards'),
    path('forwards/', views.forwards, name='forwards'),
]