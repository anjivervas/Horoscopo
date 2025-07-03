from telegram.ext import Application, CommandHandler

from app.settings import Config
from app.app_log import get_logger
from app.bot.commands import start, aries, tauro, geminis, cancer, leo, virgo, libra, escorpio, capricornio, sagitario, acuario, piscis

logger = get_logger(f"[{Config().APP_NAME}]")

TOKEN = Config().TELEGRAM_BOT_KEY  

async def post_init(application: Application):
    """Función que se ejecuta después de que la aplicación se haya inicializado."""

    logger.info("🔗 Configurando el webhook del bot de Telegram...")
    await application.bot.delete_webhook(drop_pending_updates=True)

def main():    
    logger.info("🔗 Iniciando el bot de Telegram...")

    # Verifica que el token esté 
    if not TOKEN:
        logger.error("❌ No se encontró TELEGRAM_BOT_KEY en las variables de entorno")
        raise ValueError("Token de Telegram no configurado")
    else:
        logger.info("✅ Token de Telegram encontrado")

    application = Application.builder().token(TOKEN).post_init(post_init).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("aries", aries))
    application.add_handler(CommandHandler("tauro", tauro))
    application.add_handler(CommandHandler("geminis", geminis))
    application.add_handler(CommandHandler("cancer", cancer))
    application.add_handler(CommandHandler("leo", leo))
    application.add_handler(CommandHandler("virgo", virgo))
    application.add_handler(CommandHandler("libra", libra))
    application.add_handler(CommandHandler("escorpio", escorpio))
    application.add_handler(CommandHandler("sagitario", sagitario))
    application.add_handler(CommandHandler("capricornio", capricornio))
    application.add_handler(CommandHandler("acuario", acuario))
    application.add_handler(CommandHandler("piscis", piscis))
    
    try:
        application.run_polling()
        logger.info("Bot iniciado. Usa /start para ver las opciones")
    except Exception as e:
        logger.error(f"Error al iniciar el bot: {e}")
        raise e