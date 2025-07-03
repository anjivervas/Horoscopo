import json
from telegram import Update
from telegram.ext import ContextTypes

from app.core import Horoscopo, Signos
from app.app_log import get_logger
from app.settings import Config

logger = get_logger(f"[{Config().APP_NAME}: Command Module]")

async def escorpio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        prediccion = Horoscopo(Signos.ESCORPIO.value)
        logger.info(f"Enviando predicción de: {Signos.ESCORPIO.value}")
        await update.message.reply_text(prediccion.prediction)
    except Exception as e:
        logger.error(f"Error al enviar la predicción: {e}")

