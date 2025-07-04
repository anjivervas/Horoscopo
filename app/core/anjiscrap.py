import requests
from bs4 import BeautifulSoup
from typing import Optional

from app.core.signos import Signos
from app.app_log import get_logger
from app.settings import Config

logger = get_logger(f"[{Config().APP_NAME}: Scrap Module]")

class Horoscopo:
    def __init__(self, signo: Signos):
        self.signo = signo
        self.soup = self._get_soup()
        self.description = self._get_sign_description()
        self.prediction = self._get_sign_prediction()

    def _get_soup(self) -> Optional[BeautifulSoup]:         
        # Realizar la solicitud HTTP
        url = f"https://www.20minutos.es/horoscopo/{self.signo}/"
        try:        
            response = requests.get(url)
            response.raise_for_status()  # Esto lanza una excepción si hay error
            logger.debug(f"Página obtenida correctamente: {url}")
        except requests.RequestException as e:
            logger.error(f"Error al obtener la página: {e}")
            return None

        return BeautifulSoup(response.text, "html.parser")

    def _get_sign_description(self) -> Optional[str]:
        """Obtiene la descripción del signo"""
        try:
            # Busca el div que contiene la descripción en el objeto soup
            description = self.soup.find("div", {"class": "description"})
            # Convierte la descripción a texto
            text = description.text.strip()
            logger.debug(f"Descripción del signo {self.signo}: {text}")
            return text
        except AttributeError:
            logger.error("Error al obtener la descripción del signo.")
            return "Descripción no disponible."

    def _get_sign_prediction(self) -> Optional[str]:
        """Obtiene la predicción del signo"""

       #if not self.soup:
        #    return "Predicción no disponible"

        try:
            # Obtiene todos los div que contiene la clase "descripción" (hay dos en la página)
            prediction_blocks = self.soup.find_all("div", {"class": "prediction"})
            second_prediction_block = prediction_blocks[1]
            specific_div = second_prediction_block.find("div", {"style": "padding-bottom: 1em;"})
            prediction = specific_div.text.strip()
            logger.debug(f"Predicción del signo {self.signo}: {prediction}")
            return prediction
        except (AttributeError, IndexError):
            logger.error("Error al obtener la predicción del signo.")
            return None

    def to_ditc(self):
        result = {
            "signo": self.signo,
            "prediccion": self.prediction,
            "descripcion": self.description
        }
        logger.debug(f"Devolviendo resultado en formato diccionario: {result}")
        return result