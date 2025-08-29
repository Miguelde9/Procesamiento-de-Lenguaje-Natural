import re
from collections import Counter
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TextoAnalizadoForm
from .models import TextoAnalizado
from .utils import procesar_texto  # Importar la nueva función de utilidades

def subir_texto(request):
    if request.method == 'POST':
        form = TextoAnalizadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_textos')
    else:
        form = TextoAnalizadoForm()
    return render(request, 'subir.html', {'form': form})

def lista_textos(request):
    textos = TextoAnalizado.objects.all().order_by('-fecha_subida')
    return render(request, 'lista.html', {'textos': textos})

def analizar_texto(request, texto_id):
    texto_obj = get_object_or_404(TextoAnalizado, id=texto_id)
    
    # Leer el contenido del archivo
    try:
        with texto_obj.archivo.open('r') as archivo:
            contenido = archivo.read()
    except:
        contenido = ""
    
    # Procesar el texto usando la nueva funcionalidad de limpieza
    resultado = procesar_texto(contenido)
    
    return render(request, 'resultado.html', {
        'texto': texto_obj,
        'palabras_comunes': resultado['palabras_comunes'],
        'total_palabras': resultado['total_palabras']
    })