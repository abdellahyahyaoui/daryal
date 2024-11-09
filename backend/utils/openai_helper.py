import openai
import logging

# Configura la clave de API para OpenAI directamente (solo para pruebas)
openai.api_key = "aqui debes poner la clave que te voy a dar"

def obtener_respuesta_gpt(prompt):
    try:
        # Utiliza el modelo GPT-3.5 Turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente experto en diagnóstico de vehículos."},
                {"role": "user", "content": prompt}
            ]
        )
        # Obtén y devuelve la respuesta generada
        return response['choices'][0]['message']['content'].strip()
    
    except Exception as e:
        logging.error(f"Error al hacer la solicitud a la API: {str(e)}")
        raise

# Ejemplo de uso
if __name__ == "__main__":
    prompt = "Mi coche hace un ruido extraño cuando acelero, ¿qué puede ser?"
    respuesta = obtener_respuesta_gpt(prompt)
    print(respuesta)
