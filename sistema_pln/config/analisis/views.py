import re
from collections import Counter
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TextoAnalizadoForm
from .models import TextoAnalizado
from .stopwords import STOPWORDS  # Importar desde el archivo separado

def limpiar_texto(texto):
    """
    Función para limpiar el texto:
    1. Convertir a minúsculas
    2. Eliminar símbolos de puntuación
    3. Eliminar stopwords en español
    """
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Eliminar símbolos de puntuación y caracteres especiales
    texto_limpio = re.sub(r'[^\w\s]', ' ', texto)
    
    # Tokenizar y eliminar stopwords
    palabras = texto_limpio.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra not in STOPWORDS and len(palabra) > 1]
    
    return palabras_filtradas

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
    
    # Limpiar el texto antes de procesarlo
    palabras_limpias = limpiar_texto(contenido)
    
    # Generar histograma con el texto limpio
    contador_palabras = Counter(palabras_limpias)
    palabras_comunes = contador_palabras.most_common(20)  # Top 20 palabras
    
    return render(request, 'resultado.html', {
        'texto': texto_obj,
        'palabras_comunes': palabras_comunes,
        'total_palabras': len(palabras_limpias)
    })