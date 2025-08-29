import re
from collections import Counter

# Lista de stopwords en español latino (palabras vacías) - LIMPIADA DE FORMAS ESPAÑOLAS
STOPWORDS_ES_LATINO = {
    'a', 'al', 'algo', 'algún', 'alguna', 'algunas', 'alguno', 'algunos', 'ante', 'antes', 
    'como', 'con', 'contra', 'cual', 'cuando', 'de', 'del', 'desde', 'donde', 'durante', 
    'e', 'el', 'ella', 'ellas', 'ellos', 'en', 'entre', 'era', 'eran', 'es', 'esa', 'esas', 
    'ese', 'eso', 'esos', 'esta', 'estaba', 'estaban', 'estar', 'estará', 'estas', 'este', 
    'esto', 'estos', 'estuve', 'estuviera', 'estuvieran', 'estuvieron', 'estuviese', 
    'estuviesen', 'estuvimos', 'estuviste', 'estuvo', 'fue', 'fuera', 
    'fueran', 'fueron', 'fuese', 'fuesen', 'fui', 'fuimos', 'fuiste', 'ha', 'había', 
    'habían', 'habrá', 'habrán', 'habría', 'habrían', 'hace', 'hacen', 
    'hacer', 'hacerlo', 'haces', 'hacia', 'haciendo', 'hago', 'han', 'has', 'hasta', 'he', 
    'hecho', 'hemos', 'hicieron', 'hizo', 'hoy', 'hubiera', 'hubieran', 'hubieron', 
    'hubiese', 'hubiesen', 'hubo', 'igual', 'junto', 'la', 'largo', 'las', 'le', 'les', 
    'lo', 'los', 'me', 'mi', 'mia', 'mias', 'mientras', 'mio', 'mios', 'mis', 'misma', 
    'mismas', 'mismo', 'mismos', 'modo', 'mucho', 'muchos', 'muy', 'nada', 'ni', 'no', 
    'nos', 'nosotras', 'nosotros', 'nuestra', 'nuestras', 'nuestro', 'nuestros', 'nunca', 
    'o', 'otra', 'otras', 'otro', 'otros', 'para', 'pero', 'poco', 'por', 'porque', 
    'primero', 'puede', 'pueden', 'poder', 'podrá', 'podrán', 'podría', 'podrían', 'poner', 
    'por qué', 'porque', 'primer', 'pudo', 'pueda', 'pues', 'que', 'quedar', 'querer', 
    'quién', 'quien', 'quienes', 'qué', 'se', 'sea', 'sean', 'según', 'ser', 'será', 
    'serán', 'sería', 'serían', 'si', 'sí', 'siendo', 'sin', 'sino', 'sobre', 
    'solamente', 'solo', 'somos', 'son', 'soy', 'su', 'sus', 'suya', 'suyas', 'suyo', 
    'suyos', 'también', 'tampoco', 'tan', 'tanto', 'te', 'tener', 'tenga', 'tengo', 
    'tiene', 'tienen', 'toda', 'todas', 'todo', 'todos', 'tomar', 'trabajar', 'tras', 
    'tu', 'tus', 'tuve', 'tuviera', 'tuvieran', 'tuvieron', 'tuviese', 'tuviesen', 
    'tuvimos', 'tuviste', 'tuvo', 'tuya', 'tuyas', 'tuyo', 'tuyos', 'un', 
    'una', 'unas', 'uno', 'unos', 'usa', 'usar', 'uso', 'va', 'valor', 'vamos', 
    'van', 'vaya', 'veces', 'ver', 'verdad', 'verdadera', 'verdadero', 'vez', 'voy', 'yo', 'él', 
    'éramos', 'ésa', 'ésas', 'ése', 'ésos', 'ésta', 'éstas', 
    'éste', 'éstos', 'última', 'últimas', 'último', 'últimos'
}

def limpiar_texto(texto):
    """
    Limpia el texto convirtiendo a minúsculas, eliminando puntuación y stopwords
    """
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Eliminar símbolos de puntuación y caracteres especiales, mantener letras, números y espacios
    texto = re.sub(r'[^\w\sáéíóúüñ]', ' ', texto)
    
    # Tokenizar (dividir en palabras)
    palabras = texto.split()
    
    # Eliminar stopwords (español latino)
    palabras_limpias = [palabra for palabra in palabras if palabra not in STOPWORDS_ES_LATINO]
    
    return palabras_limpias

def generar_histograma(texto):
    """
    Genera un histograma de palabras a partir de un texto limpio
    """
    palabras_limpias = limpiar_texto(texto)
    contador_palabras = Counter(palabras_limpias)
    return contador_palabras.most_common(20), len(palabras_limpias)