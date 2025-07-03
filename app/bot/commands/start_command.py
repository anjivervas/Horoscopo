from telegram import Update
from telegram.ext import ContextTypes

from app.app_log import get_logger
from app.core import Signos
from app.settings import Config

logger = get_logger(f"[{Config().APP_NAME}: Command Module]")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = f"""
¡Hola! Soy *{Config().APP_NAME}*, un bot creado por *{Config().AUTHOR_NAME}* como proyecto para la materia Transmisión de Datos.

Puedo proporcionarte la predicción para tu signo zodiacal del día de hoy. ¿Qué signo eres?

    • {Signos.ARIES.value}: /aries
    • {Signos.TAURO.value}: /tauro
    • {Signos.GEMINIS.value}: /geminis
    • {Signos.CANCER.value}: /cancer
    • {Signos.LEO.value}: /leo
    • {Signos.VIRGO.value}: /virgo
    • {Signos.LIBRA.value}: /libra
    • {Signos.ESCORPIO.value}: /escorpio
    • {Signos.SAGITARIO.value}: /sagitario
    • {Signos.CAPRICORNIO.value}: /capricornio
    • {Signos.ACUARIO.value}: /acuario
    • {Signos.PISCIS.value}: /piscis

¡Usa alguno de estos comandos para obtener la predicción del día!
    """
    # Enviar el mensaje de bienvenida al usuario
    await update.message.reply_text(welcome_text, parse_mode='Markdown')
    logger.info("Enviado mensaje de bienvenida al usuario")