import logging
from flask import Blueprint, request, jsonify
from utils.openai_helper import obtener_respuesta_gpt

api = Blueprint('api', __name__)
logging.basicConfig(level=logging.DEBUG)
MAX_QUESTION_LENGTH = 150  # Máxima longitud de la pregunta en caracteres

@api.route('/iniciar-diagnostico', methods=['POST'])
def iniciar_diagnostico():
    logging.debug(f"Received data: {request.json}")
    data = request.json
    try:
        prompt = f"Un coche {data.get('marca', 'desconocida')} {data.get('modelo', 'desconocido')} del año {data.get('año', 'desconocido')} con motor de {data.get('combustible', 'desconocido')} presenta el siguiente problema: {data.get('problema', 'No se proporcionó descripción del problema')}. Genera una pregunta para obtener más información sobre el problema."
        logging.debug(f"Generated prompt: {prompt}")
        pregunta = obtener_respuesta_gpt(prompt)
        logging.debug(f"Generated question: {pregunta}")
        return jsonify({"pregunta": pregunta})
    except Exception as e:
        logging.error(f"Error in iniciar_diagnostico: {str(e)}")
        return jsonify({"error": str(e)}), 500

@api.route('/continuar-diagnostico', methods=['POST'])
def continuar_diagnostico():
    logging.debug(f"Received data for continuation: {request.json}")
    data = request.json
    try:
        historial = data.get('historial', [])
        numero_pregunta = len([item for item in historial if item['tipo'] == 'pregunta']) + 1
        info_vehiculo = data.get('vehiculo', {})

        if numero_pregunta <= 5:
            prompt = f"""
            Basándote en la siguiente información del vehículo y el historial de preguntas y respuestas, 
            genera la pregunta número {numero_pregunta} para continuar el diagnóstico. 
            La pregunta debe ser específica para el vehículo en cuestión, breve y precisa, y no debe exceder los {MAX_QUESTION_LENGTH} caracteres.
            Si la última respuesta del usuario no está relacionada con el problema del vehículo, genera una nueva pregunta relevante sin hacer referencia a la respuesta irrelevante.
            
            Información del vehículo: {info_vehiculo}
            Historial: {historial}
            """
            logging.debug(f"Generated prompt for continuation: {prompt}")
            siguiente_pregunta = obtener_respuesta_gpt(prompt)
            
            # Asegurar que la pregunta no exceda la longitud máxima
            siguiente_pregunta = siguiente_pregunta[:MAX_QUESTION_LENGTH]
            
            logging.debug(f"Generated next question: {siguiente_pregunta}")
            return jsonify({"pregunta": siguiente_pregunta, "es_ultima": numero_pregunta == 5})
        else:
            prompt = f"""
            Basándote en toda la información recopilada sobre el vehículo y el historial de preguntas y respuestas, 
            proporciona un diagnóstico final resumido en menos de 100 caracteres, seguido de 2-3 posibles soluciones breves.
            
            Información del vehículo: {info_vehiculo}
            Historial: {historial}
            
            Formato de respuesta:
            Diagnóstico: [Diagnóstico resumido en menos de 100 caracteres]
            Soluciones:
            1. [Primera solución breve]
            2. [Segunda solución breve]
            3. [Tercera solución breve (opcional)]
            """
            logging.debug(f"Generated prompt for final diagnosis: {prompt}")
            respuesta_final = obtener_respuesta_gpt(prompt)
            logging.debug(f"Generated final diagnosis and solutions: {respuesta_final}")
            return jsonify({"diagnostico_y_soluciones": respuesta_final})
    except Exception as e:
        logging.error(f"Error in continuar_diagnostico: {str(e)}")
        return jsonify({"error": str(e)}), 500