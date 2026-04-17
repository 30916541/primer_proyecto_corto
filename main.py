import os
from dotenv import load_dotenv
from groq import Groq

def interactuar_con_llm():
    """
    Programa que se conecta al modelo llama-3.3-70b-versatile, 
    envía un prompt y muestra la respuesta.
    """
    
    # Conectar con el LLM.
    # 1.-) Para conectarse al LLM, se debe usar la clave de API proporcionada por Groq.
    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("Error: No se encontró la variable de entorno GROQ_API_KEY.")
        return

    # 2.-) Iniciar el cliente de Groq con la clave de API.
    cliente = Groq(api_key=api_key)

    print("=== Conectado a llama-3.3-70b-versatile ===")
    
    # 3.-) El usuario ingresa un mensaje (prompt).
    prompt_usuario = input("\nIngresa tu mensaje (prompt): ")

    try:
        print("\nProcesando...")
        
        # 4.-) El programa envía el prompt al LLM.
        # 5.-) El modelo de lenguaje a emplear será llama-3.3-70b-versatile.
        respuesta_llm = cliente.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt_usuario,
                }
            ],
            model="llama-3.3-70b-versatile",
        )

        # 6.-) El LLM procesa el mensaje y genera una respuesta.
        contenido_respuesta = respuesta_llm.choices[0].message.content

        # 7.-) El programa recibe la respuesta y la muestra al usuario.
        print("\n--- Respuesta del Modelo ---")
        print(contenido_respuesta)
        print("----------------------------\n")

    # 8.-) El programa maneja posibles errores de conexión o procesamiento.
    except Exception as e:
        print(f"\nOcurrió un error al comunicarse con el LLM: {e}")

# 9.-) El programa se ejecuta en un entorno local, y el usuario puede interactuar con el LLM a través de la terminal.
if __name__ == "__main__":
    
    # Ejecutar la función principal para interactuar con el LLM.
    interactuar_con_llm()