# 1. Instalamos y cargamos la librería en la nube
!pip install -q google-genai

import os
from google import genai

# 2. Tu clave secreta (deja las comillas)
os.environ["GEMINI_API_KEY"] = "PUT_HERE_YOUR_GEMINI_API_KEY"

def analizar_sentimiento(texto):
    try:
        client = genai.Client()
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Analiza el sentimiento de esta frase. Responde SOLO con una palabra (Positivo, Negativo o Neutro): {texto}"
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

# 3. EL PROYECTO REAL: Una lista de comentarios de clientes del trabajo
comentarios_clientes = [
    "El servicio ha sido fantástico y me han atendido super rápido.",
    "Vaya desastre de producto, no funciona y ha llegado roto.",
    "El paquete llegó el miércoles, tal y como estaba programado.",
    "No me gusta nada la nueva actualización, es muy confusa.",
    "Me encanta cómo funciona, os voy a recomendar a mis compañeros."
]

print("Iniciando el analizador de opiniones de clientes...\n")

# El programa lee la lista una por una, le pregunta a Gemini y nos muestra el resultado
for i, frase in enumerate(comentarios_clientes, 1):
    resultado = analizar_sentimiento(frase)
    print(f"Comentario #{i}: '{frase}'")
    print(f"👉 Análisis de Gemini: {resultado}")
    print("-" * 50) # Esto solo pinta una línea de separación

print("\n¡PROYECTO COMPLETADO CON ÉXITO!")
