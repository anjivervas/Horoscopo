import requests
from bs4 import BeautifulSoup

def get_soup(signo):
     # URL base de página de horóscopos (signo específico)
    url = f"https://www.20minutos.es/horoscopo/{signo}/"
    
    # Realizar la solicitud HTTP
    try:        
        response = requests.get(url)
        response.raise_for_status()  # Esto lanza una excepción si hay error
    except requests.RequestException as e:
        print(f"Error al obtener la página: {e}")
        return None

    return BeautifulSoup(response.text, "html.parser")

def get_sign_description(soup: BeautifulSoup) -> str:
    """Obtiene la descripción del signo"""
    
    # Busca el div que contiene la descripción en el objeto soup
    description = soup.find("div", {"class": "description"})
    
    # Convierte la descripción a texto
    text = description.text.strip()
    
    return text

def get_sign_prediction(soup: BeautifulSoup) -> str:
    """Obtiene la predicción del signo"""

    # Obtiene todos los div que contiene la clase "descripción" (hay dos en la página)
    prediction_blocks = soup.find_all("div", {"class": "prediction"})
    second_prediction_block = prediction_blocks[1]
    specific_div = second_prediction_block.find("div", {"style": "padding-bottom: 1em;"})
    prediction = specific_div.text.strip()
    return prediction

if __name__ == "__main__":
    signo = "leo"
    soup = get_soup(signo)
    prediccion = get_sign_prediction(soup)
    print(f"Predicción de: {signo}\n\n")
    print(prediccion)
