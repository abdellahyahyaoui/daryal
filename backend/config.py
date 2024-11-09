# import os
# from dotenv import load_dotenv
# import logging

# load_dotenv()

# class Config:
#     OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#     if not OPENAI_API_KEY:
#         logging.error("No OPENAI_API_KEY set for application")
#         raise ValueError("No OPENAI_API_KEY set for application")
#     else:
#         logging.debug("OPENAI_API_KEY loaded successfully")

# # Configura la clave API para OpenAI
# import openai
# openai.api_key = Config.OPENAI_API_KEY
# try:
#     response = openai.Completion.create(
#         engine="text-davinci-003",  # Asegúrate de usar el motor correcto
#         prompt="Hello, world!",
#         max_tokens=5
#     )
#     print(response.choices[0].text.strip())
# except Exception as e:
#     logging.error(f"Error al hacer la solicitud a la API: {e}")