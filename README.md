# 🚀 Analizador de Sentimientos con Gemini 2.5 Flash

Este proyecto automatiza la clasificación de textos y opiniones de clientes utilizando Inteligencia Artificial.

## 🛠️ Características y Desafíos Superados
El proyecto fue diseñado inicialmente para entorno local, pero debido a restricciones estrictas de Firewall y políticas de red corporativas (errores de resolución de DNS y bloqueos de terminal), se adaptó con éxito para ser ejecutado en entornos Cloud mediante *Google Colab*. 

Esto permite realizar peticiones HTTPS nativas a la API de Google sin depender de configuraciones de Proxy o credenciales locales del sistema.

## 🧰 Tecnologías Utilizadas
* Python 3
* Google GenAI SDK (gemini-2.5-flash)
* Google Colab (Entorno Cloud de ejecución)
* GitHub para control de versiones

## 📋 Cómo Ejecutarlo
1. Abre el script en cualquier entorno compatible con Python (preferiblemente Google Colab si te encuentras bajo redes corporativas restrictivas).
2. Instala la librería oficial: pip install google-genai
3. Configura tu variable de entorno con la clave de Google AI Studio.
4. Ejecuta el script para procesar listas de textos en masa.
