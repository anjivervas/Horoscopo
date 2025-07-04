from enum import StrEnum

class Signos(StrEnum):
    ARIES="aries"
    TAURO="tauro"
    GEMINIS="geminis"
    CANCER="cancer"
    LEO="leo"
    VIRGO="virgo"
    LIBRA="libra"
    ESCORPIO="escorpio"
    SAGITARIO="sagitario"
    CAPRICORNIO="capricornio"
    ACUARIO="acuario"
    PISCIS="piscis"

    def __repr__(self):
        """Representación del signo zodiacal."""
        return f"Signos.{self.name.upper()}"

    def signo(self):
        """Retorna el nombre del signo zodiacal."""
        return self.value

    def descripcion(self):
        """Retorna la descripción del signo zodiacal"""
        descripciones = {
            "aries": "Aries es un signo de fuego, conocido por su energía y pasión.",
            "tauro": "Tauro es un signo de tierra, asociado con la estabilidad y la sensualidad.",
            "geminis": "Géminis es un signo de aire, caracterizado por su dualidad y curiosidad.",
            "cancer": "Cáncer es un signo de agua, conocido por su sensibilidad y empatía.",
            "leo": "Leo es un signo de fuego, famoso por su liderazgo y creatividad.",
            "virgo": "Virgo es un signo de tierra, asociado con el análisis y la perfección.",
            "libra": "Libra es un signo de aire, conocido por su búsqueda de equilibrio y armonía.",
            "escorpio": "Escorpio es un signo de agua, famoso por su intensidad y misterio.",
            "sagitario": "Sagitario es un signo de fuego, asociado con la aventura y la filosofía.",
            "capricornio": "Capricornio es un signo de tierra, conocido por su ambición y disciplina.",
            "acuario": "Acuario es un signo de aire, famoso por su originalidad y humanitarismo.",
            "piscis": "Piscis es un signo de agua, asociado con la intuición y la espiritualidad."
        }
        return descripciones.get(self.value, "Descripción no disponible.")