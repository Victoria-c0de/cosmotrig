# cosmotrig_app/views.py
from django.shortcuts import render

def seccion_historica(request):
    # Lógica para la sección histórica
    return render(request, 'cosmotrig_app/seccion_historica.html')

def seccion_trigonometria(request):
    # Lógica para la sección de trigonometría
    return render(request, 'cosmotrig_app/seccion_trigonometria.html')

def ventana_tinker(request):
    # Lógica para la ventana Tinker
    return render(request, 'cosmotrig_app/calculadora_triangulo.html')

def seccion_simulacion(request):
    # Lógica para la sección de simulación
    return render(request, 'cosmotrig_app/seccion_simulacion.html')
