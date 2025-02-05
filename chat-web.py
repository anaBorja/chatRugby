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



# Preguntas con estilos y funcionalidad de clic
questions = [
    ("¿Cuáles son las curiosidades más interesantes del rugby?", "#ff5722"),
    ("¿Qué ciudades son anfitrionas de la Rugby World Cup 2027?", "#e67e22"),
    ("¿Cuántos equipos participan?", "#e59866"),
    ("¿Las fechas de la clasificación de Europa?", "#f0b27a"),
    ("¿Qué anunció World Rugby el 30 de enero de 2025 sobre las ciudades anfitrionas?", "#f5b041"),
]

# Columna derecha con sugerencias de preguntas
st.sidebar.header("Ejemplos de preguntas")

# Generar los divs clickeables usando HTML + JavaScript
st.sidebar.markdown(
    """
    <script>
    function sendQuestion(question) {
        var streamlitDoc = window.parent.document;
        var inputBox = streamlitDoc.querySelector('textarea');
        var event = new Event('input', { bubbles: true });
        inputBox.value = question;
        inputBox.dispatchEvent(event);
    }
    </script>
    """,
    unsafe_allow_html=True,
)

# Crear los divs de preguntas con clics
for question, color in questions:
    st.sidebar.markdown(
        f"""
        <div onclick="sendQuestion('{question}')" 
             style="background-color: {color}; padding: 10px; margin-bottom: 10px; border-radius: 5px; 
             color: white; font-weight: bold; cursor: pointer; text-align: center;">
            {question}
        </div>
        """,
        unsafe_allow_html=True,
    )






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