# 🔮 HoróscopoBot

> Bienvenido al repositorio de HoróscopoBot, un bot de Telegram diseñado para ofrecerte las predicciones diarias de tu signo zodiacal.

Este bot se conecta a una fuente externa (20minutos.es) para obtener la información más reciente a través de web scraping y la presenta de manera sencilla y accesible directamente en tus chats de Telegram.# HOROSCOPO BOT


## ✨ Características

- *Predicciones Diarias:* Obtén tu horóscopo actualizado cada día para cualquier signo del zodiaco.

- *Interfaz de Comandos Sencilla:* Interactúa con el bot usando comandos intuitivos de Telegram para solicitar horóscopos específicos.

- *Logging Detallado:* Un sistema de logging robusto que registra la actividad del bot y cualquier incidencia para facilitar el monitoreo y la depuración.

- *Configuración Flexible:* Personaliza fácilmente el comportamiento del bot a través de variables de entorno, incluyendo el token de Telegram, el nivel de logging y la URL de la fuente de datos.

- *Arquitectura Modular:* El código está organizado en módulos lógicos para una mejor mantenibilidad y escalabilidad.

### 📋 Requisitos

> Para ejecutar HoróscopoBot, necesitarás lo siguiente:

- Python 3.8+
- Un token de bot de Telegram (obtenido de BotFather)

> Las dependencias de Python listadas en requirements.txt:

- python-telegram-bot
- requests
- beautifulsoup4
- python-dotenv

[Y otras librerías auxiliares para logging y gestión de entorno.]
```bash
# Clona el repositorio (o descarga los archivos del proyecto)
git clone https://github.com/anjivervas/Horoscopo
cd horoscopobot

# Crea un entorno virtual (recomendado) e instálalo:
python -m venv venv

# En Windows:
.\venv\Scripts\activate

# Instala las dependencias del proyecto:
pip install -r requirements.txt
```


## ⚙️ Configuración


#### Sigue estos pasos para configurar y poner en marcha el bot:

- Clona el repositorio (o descarga los archivos del proyecto).

#### Crea un entorno virtual (recomendado) e instálalo:
```bash
- python -m venv venv
###### En Windows:
.\venv\Scripts\activate

#### Instala las dependencias del proyecto:

- pip install -r requirements.txt
```

⚠️ Crea un archivo .env en la raíz del proyecto (al mismo nivel que run.py). Este archivo contendrá tus variables de entorno. Puedes usar el archivo .env.example como plantilla.

1. `TELEGRAM_BOT_KEY="TU_TOKEN_DE_TELEGRAM_AQUI"`
2. `LOG_LEVEL="INFO" # Puedes cambiar a DEBUG, WARNING, ERROR`
3. `URL_BASE="https://www.20minutos.es/horoscopo/"`
4. `APP_NAME="HoroscopoBot"`
5. `AUTHOR_NAME="Anjiver"`

- Reemplaza "TU_TOKEN_DE_TELEGRAM_AQUI" con el token que te proporcionó BotFather.

- Ajusta LOG_LEVEL según tus necesidades de registro.

- URL_BASE, APP_NAME y AUTHOR_NAME pueden dejarse con sus valores por defecto o ser personalizados.

## 🚀 Comandos Disponibles

Una vez que el bot esté en funcionamiento, puedes interactuar con él en Telegram usando los siguientes comandos:

- /start: Inicia la conversación con el bot y recibe un mensaje de bienvenida.

- /aries: Obtiene la predicción del horóscopo para Aries.

- /tauro: Obtiene la predicción del horóscopo para Tauro.

- /geminis: Obtiene la predicción del horóscopo para Géminis.

- /cancer: Obtiene la predicción del horóscopo para Cáncer.

- /leo: Obtiene la predicción del horóscopo para Leo.

- /virgo: Obtiene la predicción del horóscopo para Virgo.

- /libra: Obtiene la predicción del horóscopo para Libra.

- /escorpio: Obtiene la predicción del horóscopo para Escorpio.

- /sagitario: Obtiene la predicción del horóscopo para Sagitario.

- /capricornio: Obtiene la predicción del horóscopo para Capricornio.

- /acuario: Obtiene la predicción del horóscopo para Acuario.

- /piscis: Obtiene la predicción del horóscopo para Piscis.


## 💬 Ejemplo de Uso

Para obtener tu horóscopo, simplemente abre un chat con el bot en Telegram y envía el comando correspondiente a tu signo. Por ejemplo:

```bash
# Iniciara el bot y enviara una lista de los signos zodiacales.
/star

# El bot responderá con la predicción del día para Leo.
/leo
```


## 📊 Estructura de Salida

Cuando envías un comando de signo zodiacal, el bot te devolverá un mensaje de texto con la predicción del horóscopo obtenida de la fuente externa. 

> La estructura del mensaje será un texto plano con la predicción directamente.

🏁 *¡Espero que disfrutes usando HoróscopoBot!* 

> ¡Que los astros te sean favorables!


## 📄 Licencia

MIT © [Anjivervas](https://github.com/anjivervas/Horoscopo)[text](../OneDrive/Documentos/uni/proyecto_app/README.md)