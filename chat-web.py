import streamlit as st
from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

# Cargar las variables de configuración desde el archivo .env
load_dotenv()
ai_endpoint = st.secrets['AI_SERVICE_ENDPOINT']
ai_key = st.secrets['AI_SERVICE_KEY']
ai_project_name = st.secrets['QA_PROJECT_NAME']
ai_deployment_name =st.secrets['QA_DEPLOYMENT_NAME']

# Crear el cliente utilizando el endpoint y la clave
credential = AzureKeyCredential(ai_key)
ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)


# Título de la aplicación
st.title("🗿Chatbot de Rugby World Cup 2027")

# Cuadro con contexto
st.info("💬 Este chatbot responde preguntas sobre la Rugby World Cup 2027. Pregunta sobre curiosidades de rugby, ciudades anfitrionas y más.")

# Espacio para mostrar el historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos como una conversación
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Columna derecha con sugerencias de preguntas
st.sidebar.header("Ejemplos de preguntas")

# Agregar las preguntas dentro de cajitas de colores
st.sidebar.markdown("""
<div style="background-color: #ff5722; padding: 10px; margin-bottom: 10px; border-radius: 5px; color: white; font-weight: bold;">
    ¿Cuáles son las curiosidades más interesantes del rugby?
</div>
<div style="background-color: #e67e22; padding: 10px; margin-bottom: 10px; border-radius: 5px; color: white; font-weight: bold;">
    ¿Qué ciudades son anfitrionas de la Rugby World Cup 2027?
</div>
<div style="background-color: #e59866 ; padding: 10px; margin-bottom: 10px; border-radius: 5px; color: white; font-weight: bold;">
    ¿Cuántos equipos participan?
</div>
<div style="background-color: #f0b27a; padding: 10px; margin-bottom: 10px; border-radius: 5px; color: white; font-weight: bold;">
    ¿Las fechas de la clasificacion de Europa?
</div>
<div style="background-color: #f5b041; padding: 10px; margin-bottom: 10px; border-radius: 5px; color: white; font-weight: bold;">
    ¿Qué anunció World Rugby el 30 de enero de 2025 sobre las ciudades anfitrionas?
</div>
""", unsafe_allow_html=True)


# Caja de texto para entrada del usuario
if user_input := st.chat_input("Escribe tu pregunta aquí..."):
    # Mostrar inmediatamente la pregunta del usuario
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        # Llamar al servicio Question Answering de Azure
        response = ai_client.get_answers(
            project_name=ai_project_name,
            deployment_name=ai_deployment_name,
            question=user_input,
        )

        # Verificar si se obtuvo una respuesta
        if response.answers:
            answer = response.answers[0].answer  # Tomamos la primera respuesta
        else:
            answer = "Lo siento, no pude encontrar una respuesta a esa pregunta."

    except Exception as e:
        answer = f"Hubo un error al procesar la pregunta: {e}"

    # Mostrar inmediatamente la respuesta del chatbot
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Guardar la respuesta en la sesión
    st.session_state.messages.append({"role": "assistant", "content": answer})