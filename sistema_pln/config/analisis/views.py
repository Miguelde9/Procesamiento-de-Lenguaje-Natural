import re
from collections import Counter
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TextoAnalizadoForm
from .models import TextoAnalizado
from .utils import generar_histograma, limpiar_texto  # Importar las nuevas funciones

def subir_texto(request):
    if request.method == 'POST':
        form = TextoAnalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_textos')
    else:
        form = TextoAnalizadoForm()
    return render(request, 'analisis/subir.html', {'form': form})

def lista_textos(request):
    textos = TextoAnalizado.objects.all().order_by('-fecha_subida')
    return render(request, 'analisis/lista.html', {'textos': textos})

def analizar_texto(request, texto_id):
    texto_obj = get_object_or_404(TextoAnalizado, id=texto_id)
    
    # Leer el contenido del archivo
    try:
        with texto_obj.archivo.open('r', encoding='utf-8') as archivo:
            contenido = archivo.read()
    except:
        try:
            with texto_obj.archivo.open('r', encoding='latin-1') as archivo:
                contenido = archivo.read()
        except:
            contenido = ""
    
    # Obtener palabras limpias para mostrar
    palabras_limpias = limpiar_texto(contenido)
    
    # Generar histograma usando la nueva función
    palabras_comunes, total_palabras_limpias = generar_histograma(contenido)
    
    return render(request, 'analisis/resultado.html', {
        'texto': texto_obj,
        'palabras_comunes': palabras_comunes,
        'total_palabras': total_palabras_limpias,  # Cambiado a total_palabras para coincidir con la plantilla
        'palabras_limpias': palabras_limpias[:50]  # Mostrar solo las primeras 50 palabras limpias
    })