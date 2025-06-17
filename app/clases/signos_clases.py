import requests
from bs4 import BeautifulSoup
from typing import Optional

class HoroscopeScraper:
    BASE_URL = "https://www.20minutos.es/horoscopo/{sign}/"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...'
        })
    
    def get_soup(self, sign: str) -> Optional[BeautifulSoup]:
        """Obtiene el objeto BeautifulSoup para un signo específico"""
        url = self.BASE_URL.format(sign=sign)
        
        try:        
            response = self.session.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"Error al obtener la página: {e}")
            return None

class HoroscopeParser:
    @staticmethod
    def get_sign_description(soup: BeautifulSoup) -> str:
        """Obtiene la descripción general del signo"""
        description = soup.find("div", {"class": "description"})
        return description.text.strip() if description else "Descripción no disponible"
    
    @staticmethod
    def get_daily_prediction(soup: BeautifulSoup) -> str:
        """Obtiene la predicción diaria del signo"""
        prediction_blocks = soup.find_all("div", {"class": "prediction"})
        
        if len(prediction_blocks) > 1:
            second_block = prediction_blocks[1]
            specific_div = second_block.find("div", {"style": "padding-bottom: 1em;"})
            return specific_div.text.strip() if specific_div else "Predicción no disponible"
        
        return "Predicción no disponible"

class Horoscope:
    def __init__(self, sign: str):
        self.sign = sign.lower()
        self.scraper = HoroscopeScraper()
        self.parser = HoroscopeParser()
        self.soup = None
    
    def fetch_data(self) -> bool:
        """Obtiene los datos del horóscopo"""
        self.soup = self.scraper.get_soup(self.sign)
        return self.soup is not None
    
    def get_description(self) -> str:
        """Devuelve la descripción del signo"""
        if not self.soup:
            if not self.fetch_data():
                return "No se pudo obtener la descripción"
        return self.parser.get_sign_description(self.soup)
    
    def get_prediction(self) -> str:
        """Devuelve la predicción diaria"""
        if not self.soup:
            if not self.fetch_data():
                return "No se pudo obtener la predicción"
        return self.parser.get_daily_prediction(self.soup)
    
    def display(self):
        """Muestra la información del horóscopo"""
        if not self.soup and not self.fetch_data():
            print(f"No se pudo obtener información para {self.sign}")
            return
        
        print(f"\nHoróscopo de {self.sign.capitalize()}")
        print("\nDescripción:")
        print(self.get_description())
        print("\nPredicción diaria:")
        print(self.get_prediction())
        print("-" * 50)

if __name__ == "__main__":
    # Ejemplo de uso
    signo = "leo"
    horoscopo = Horoscope(signo)
    horoscopo.display()