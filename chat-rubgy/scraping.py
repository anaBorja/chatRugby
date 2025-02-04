import requests
from bs4 import BeautifulSoup
import json

# Define las URLs de los partidos, ciudades y noticias
urls = {
    "partidos": [
        "https://www.rugbyworldcup.com/2027/en/qualifying",
        "https://www.rugbyworldcup.com/2027/en/qualifying/europe",
        "https://www.rugbyworldcup.com/2027/en/qualifying/asia",
        "https://www.rugbyworldcup.com/2027/en/qualifying/africa",
        "https://www.rugbyworldcup.com/2027/en/qualifying/america-pacific",
        "https://www.rugbyworldcup.com/2027/en/qualifying/final"
    ],
    "ciudades": [
        "https://www.rugbyworldcup.com/2027/en/host-cities/adelaide-tarntanya",
        "https://www.rugbyworldcup.com/2027/en/host-cities/brisbane-meeanjin",
        "https://www.rugbyworldcup.com/2027/en/host-cities/melbourne-narrm",
        "https://www.rugbyworldcup.com/2027/en/host-cities/newcastle-awabakal-worimi",
        "https://www.rugbyworldcup.com/2027/en/host-cities/perth-boorloo",
        "https://www.rugbyworldcup.com/2027/en/host-cities/sydney-gadigal",
        "https://www.rugbyworldcup.com/2027/en/host-cities/townsville-gurambilbarra"
    ],
    "noticias": [
        "https://www.rugbyworldcup.com/2027/en/news"
    ]
}

def get_page_data(url):
    """Obtiene los datos de una página usando BeautifulSoup."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extrae el contenido relevante de la página, dependiendo de la estructura HTML
    return soup.get_text()

# Extrae los datos para cada sección
partidos_data = [get_page_data(url) for url in urls["partidos"]]
ciudades_data = [get_page_data(url) for url in urls["ciudades"]]
noticias_data = get_page_data(urls["noticias"][0])  # Solo una URL para noticias

def clean_text(data):
    """Limpia el texto eliminando saltos de línea y caracteres no deseados"""
    return " ".join(data.split())

# Función para preparar el formato QnA
def prepare_qna_format(url, data):
    """Prepara las preguntas y respuestas según la URL y el contenido extraído"""
    clean_data = clean_text(data)  # Limpiar los datos antes de agregarlos

    qna = []
    if "qualifying" in url:
        qna.append({
            "questions": ["¿Cuáles son los partidos de clasificación?"],
            "answer": clean_data  # Corregido: "answer" en lugar de "answers"
        })
    elif "host-cities" in url:
        qna.append({
            "questions": ["¿Cuáles son las ciudades anfitrionas?"],
            "answer": clean_data
        })
    elif "news" in url:
        qna.append({
            "questions": ["¿Cuáles son las últimas noticias?"],
            "answer": clean_data
        })
    
    return qna

# Función para guardar los datos en formato TXT
def save_to_text(qna_data, filename='qna_data.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in qna_data:
            # Escribe la pregunta y la respuesta en el archivo
            f.write(f"Pregunta: {item['questions'][0]}\n")
            f.write(f"Respuesta: {item['answer']}\n\n")

# Guardar los datos procesados en el archivo TXT
def save_data_as_txt():
    all_qna_data = []

    # Para partidos
    for url in urls["partidos"]:
        data = get_page_data(url)
        all_qna_data.extend(prepare_qna_format(url, data))

    # Para ciudades
    for url in urls["ciudades"]:
        data = get_page_data(url)
        all_qna_data.extend(prepare_qna_format(url, data))

    # Para noticias
    for url in urls["noticias"]:
        data = get_page_data(url)
        all_qna_data.extend(prepare_qna_format(url, data))

    # Guardamos en formato TXT
    save_to_text(all_qna_data)

# Llamamos a la función para guardar los datos en formato TXT
save_data_as_txt()

print("Datos guardados correctamente en qna_data.txt.")
