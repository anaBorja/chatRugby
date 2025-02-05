# 🏉 Chatbot de la Rugby World Cup 2027 con Azure AI Language Service

Este es un **chatbot basado en Azure AI Language Service** que responde preguntas sobre la **Rugby World Cup 2027**. Utiliza el servicio **Custom Question Answering** para proporcionar respuestas a preguntas sobre equipos, partidos, estadios y más.  


Actualmente, está **desplegado en Streamlit** y puedes probarlo aquí:  

👉 **[PRUÉBALO AHORA](https://rubgychat.streamlit.app/)** 🚀  


---

## 🚀 1️⃣ Preparación en Azure: Configurar Recursos

Antes de ejecutar este chatbot, debes preparar los recursos en **Azure AI Language Services**:

### 🔹 **Paso 1: Crear el servicio Azure AI Language**
1. Ve al **Portal de Azure**: [https://portal.azure.com](https://portal.azure.com)
2. Crea un recurso de **Azure AI Language**.
3. Guarda el **endpoint** y la **clave de acceso**, ya que los necesitarás más adelante.

### 🔹 **Paso 2: Crear un Proyecto de Custom Question Answering**
1. Entra en **Azure AI Language Studio**.
2. Crea un **proyecto nuevo** y añade datos de preguntas y respuestas sobre la Rugby World Cup 2027.
3. Despliega el proyecto y anota el **nombre del proyecto** y el **nombre del despliegue**.

---

## 🖥 2️⃣ Instalación y Configuración Local

### 🔹 **Paso 1: Clona este repositorio**
```bash
git clone https://github.com/anaBorja/chatRugby.git
cd chatRugby
```
### 🔹 Paso 2: Instala las dependencias
Asegúrate de tener **Python 3.8+** y ejecuta:

```bash
pip install -r requirements.txt
```
### 🔹 Paso 3:  Configura las credenciales de Azure
Crea un archivo .env en la raíz del proyecto con el siguiente contenido:
```bash
AI_SERVICE_ENDPOINT=tu_endpoint
AI_SERVICE_KEY=tu_api_key
QA_PROJECT_NAME=tu_nombre_de_proyecto
QA_DEPLOYMENT_NAME=tu_nombre_de_despliegue

```
---
## 🌍 3️⃣ Despliegue en Streamlit
Este chatbot ya está desplegado en Streamlit. Para ejecutarlo localmente, usa el siguiente comando:
```bash
streamlit run chat-web.py

```
Si deseas desplegar tu propia versión, sigue estos pasos:

### ☁️ **Cómo desplegar en Streamlit Cloud**
1. **Sube tu código** a un repositorio en **GitHub**.
2. **Accede a Streamlit Cloud**:  
   Ve a 👉 [Streamlit Community Cloud](https://share.streamlit.io/)
3. **Haz clic en "New App"** y selecciona tu repositorio.
4. **Configura las variables de entorno** en **Secrets**:
   - Ve a **"Advanced settings"** y abre **"Secrets"**.
   - Agrega las siguientes claves con tus valores de Azure:

     ```ini
     AI_SERVICE_ENDPOINT=tu_endpoint
     AI_SERVICE_KEY=tu_api_key
     QA_PROJECT_NAME=tu_nombre_de_proyecto
     QA_DEPLOYMENT_NAME=tu_nombre_de_despliegue
     ```

5. **Haz clic en "Deploy"** y espera a que la aplicación se inicie.

### 🎉 ¡Tu chatbot ahora estará disponible en Streamlit Cloud y podrás compartir el enlace con otros usuarios! 🏉🔥
---
# 📚 Aprende más sobre Azure AI Language Service

Si quieres aprender más sobre cómo funciona el servicio de **Azure AI Language Service** y cómo se configuran los modelos de preguntas y respuestas, consulta la documentación oficial de Microsoft en el siguiente enlace:  

🔗 **[Guía de aprendizaje de Azure AI Language Service](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/02-qna.html)**  

Este recurso te ayudará a entender mejor cómo estructurar y mejorar tu chatbot utilizando **Custom Question Answering**. 🚀

