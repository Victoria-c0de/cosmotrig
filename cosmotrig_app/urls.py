# cosmotrig_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.seccion_historica, name='seccion_historica'),
    path('seccion_trigonometria/', views.seccion_trigonometria, name='seccion_trigonometria'),
    path('ventana_tinker/', views.ventana_tinker, name='ventana_tinker'),
    path('seccion_simulacion/', views.seccion_simulacion, name='seccion_simulacion'),
]
