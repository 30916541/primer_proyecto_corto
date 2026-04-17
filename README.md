# Proyecto de Interacción con LLM usando Groq

## Descripción

Este proyecto es un script en Python que permite interactuar con un modelo de lenguaje grande (LLM) utilizando la API de Groq. El programa se conecta al modelo `llama-3.3-70b-versatile`, envía un prompt proporcionado por el usuario y muestra la respuesta generada por el modelo.

El proyecto está desarrollado como parte de un trabajo universitario para demostrar el uso de APIs de IA y el manejo de entornos virtuales en Python.

## Requisitos

- Python 3.7 o superior
- Librerías necesarias:
  - `groq` (para interactuar con la API de Groq)
  - `python-dotenv` (para cargar variables de entorno desde un archivo `.env`)

## Instalación

1. **Clona o descarga el proyecto** en tu máquina local.

2. **Crea un entorno virtual** (opcional pero recomendado):
   ```bash
   python -m venv env
   ```

3. **Activa el entorno virtual**:
   - En Linux/Mac:
     ```bash
     source env/bin/activate
     ```
   - En Windows:
     ```bash
     env\Scripts\activate
     ```

4. **Instala las dependencias**:
   ```bash
   pip install groq python-dotenv
   ```

## Configuración

1. **Obtén una clave de API de Groq**:
   - Regístrate en [Groq](https://groq.com/) y obtén tu clave de API.

2. **Crea un archivo `.env`** en la raíz del proyecto con el siguiente contenido:
   ```
   GROQ_API_KEY=tu_clave_de_api_aqui
   ```
   Reemplaza `tu_clave_de_api_aqui` con tu clave de API real.

   **Nota**: Asegúrate de que el archivo `.env` esté incluido en tu `.gitignore` para no subirlo al repositorio público.

## Uso

1. Asegúrate de que el entorno virtual esté activado.

2. Ejecuta el script principal:
   ```bash
   python main.py
   ```

3. El programa te pedirá que ingreses un mensaje (prompt). Escribe tu consulta y presiona Enter.

4. El programa procesará la solicitud y mostrará la respuesta del modelo.

## Ejemplo de Uso

```
=== Conectado a llama-3.3-70b-versatile ===

Ingresa tu mensaje (prompt): ¿Cuál es la capital de Francia?

Procesando...

--- Respuesta del Modelo ---
La capital de Francia es París.
----------------------------
```

## Manejo de Errores

- Si no se encuentra la variable de entorno `GROQ_API_KEY`, el programa mostrará un mensaje de error.
- En caso de problemas de conexión o procesamiento, se mostrará un mensaje de error con detalles.

## Estructura del Proyecto

- `main.py`: Script principal que contiene la lógica de interacción con el LLM.
- `env/`: Directorio del entorno virtual (no incluido en el repositorio).
- `.env`: Archivo de configuración con la clave de API (no incluido en el repositorio).

## Equipo de Desarrollo
- Juan Morales  C.I.: 30916541
- Omaira Rodriguez C.I.: 15351394
- Keiber Mendina C.I.: 31401788
