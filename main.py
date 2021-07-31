import logging
from telegram.ext import *
import responses

API_KEY = '1804471199:AAFPdXBOo2cN-OaF4fGHmXDHEG_K54yVwtM'

# Configurar el registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Hola! Soy una bot. ¿Qué pasa?')


def help_command(update, context):
    update.message.reply_text('¡Intente escribir cualquier cosa y haré todo lo posible para responder!')


def custom_command(update, context):
    update.message.reply_text('Este es un comando personalizado, puede agregar el texto que desee aquí.')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Respuesta del bot
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Errores de registros
    logging.error(f'Update {update} caused error {context.error}')


# Ejecutar el programa
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Comandos
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Mensajes
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Registra todos los errores
    dp.add_error_handler(error)

    # Ejecuta el bot
    updater.start_polling(1.0)
    updater.idle()
