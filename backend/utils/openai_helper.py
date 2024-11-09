import openai
import logging

# Configura la clave de API para OpenAI directamente (solo para pruebas)
openai.api_key = "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"

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