import requests
from bs4 import BeautifulSoup

class Horoscopo:
    def __init__(self, signo: str):
        self.signo = signo
        self.soup = self._get_soup()
        self.description = self._get_sign_description()
        self.prediction = self._get_sign_prediction()

    def _get_soup(self):        
        # Realizar la solicitud HTTP
        url = f"https://www.20minutos.es/horoscopo/{self.signo}/"
        try:        
            response = requests.get(url)
            response.raise_for_status()  # Esto lanza una excepción si hay error
        except requests.RequestException as e:
            print(f"Error al obtener la página: {e}")
            return None

        return BeautifulSoup(response.text, "html.parser")

    def _get_sign_description(self) -> str:
        """Obtiene la descripción del signo"""
        
        # Busca el div que contiene la descripción en el objeto soup
        description = self.soup.find("div", {"class": "description"})
        
        # Convierte la descripción a texto
        text = description.text.strip()
        
        return text

    def _get_sign_prediction(self) -> str:
        """Obtiene la predicción del signo"""

        # Obtiene todos los div que contiene la clase "descripción" (hay dos en la página)
        prediction_blocks = self.soup.find_all("div", {"class": "prediction"})
        second_prediction_block = prediction_blocks[1]
        specific_div = second_prediction_block.find("div", {"style": "padding-bottom: 1em;"})
        prediction = specific_div.text.strip()
        return prediction

if __name__ == "__main__":
    prediccion = Horoscopo("leo")
    print(prediccion.prediction)