import telebot
from telebot import types
import pyttsx3
import uuid
import os

# Token do seu bot (obtenha em https://core.telegram.org/bots:new)
BOT_TOKEN =('7617534366:AAE7kGQuG6sGwZIT6tEMwsMXSDyX3B2eWk8')

bot = telebot.TeleBot(BOT_TOKEN)
engine = pyttsx3.init()

# Dicionário para armazenar as preferências e mensagens de cada usuário
user_data = {}


# Função para criar o teclado de opções (não inline)
def create_reply_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
    markup.add(
        types.KeyboardButton("Voz Masculina"),
        types.KeyboardButton("Voz Feminina"),
        types.KeyboardButton("Não Converter")
    )
    return markup


# Função para configurar a voz
def set_voice(gender):
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')

    engine.setProperty('rate', rate - 50)

    # Corrigir para buscar o nome correto da voz conforme gênero
    if gender == "voz masculina":
        # Definir a voz masculina (ajustar conforme as vozes disponíveis no sistema)
        engine.setProperty('voice', voices[0].id)  # Pode ser necessário ajustar o índice
    elif gender == "voz feminina":
        # Definir a voz feminina (ajustar conforme as vozes disponíveis no sistema)
        engine.setProperty('voice', voices[1].id)  # Pode ser necessário ajustar o índice


# Handler para o comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Olá! Envie uma mensagem para converter em áudio e escolha a voz desejada.",
                     reply_markup=create_reply_keyboard())
    print("Bot iniciado e pronto para uso.")


# Handler para mensagens de texto (onde o usuário digita a mensagem a ser convertida)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id

    # Se o usuário digitar uma escolha de voz (em vez de uma mensagem), processar a voz
    if message.text in ["Voz Masculina", "Voz Feminina", "Não Converter"]:
        if chat_id in user_data and 'text' in user_data[chat_id]:
            user_data[chat_id]['voice'] = message.text.lower()

            # Se a escolha não for "Não Converter", realizar a conversão
            if user_data[chat_id]['voice'] != 'não converter':

                # Gera um nome de arquivo único
                filename = f"audio_{uuid.uuid4()}.mp3"

                try:
                    # Configura a voz conforme a escolha
                    set_voice(user_data[chat_id]['voice'])
                    # Converte a mensagem para áudio
                    engine.save_to_file(user_data[chat_id]['text'], filename)
                    engine.runAndWait()

                    # Envia o áudio para o usuário
                    with open(filename, 'rb') as audio:
                        bot.send_audio(chat_id, audio)

                except Exception as e:
                    bot.send_message(chat_id, f"Ocorreu um erro: {str(e)}")

                finally:
                    # Remove o arquivo temporário
                    try:
                        os.remove(filename)
                    except OSError:
                        pass
            else:
                bot.send_message(chat_id, "A mensagem não será convertida para áudio.")

        else:
            bot.send_message(chat_id, "Envie uma mensagem de texto antes de escolher a voz.")

        # Redefinir a escolha da voz para a próxima interação
        user_data[chat_id]['voice'] = None

    else:
        # Salvar a mensagem digitada pelo usuário e pedir para escolher a voz
        if chat_id not in user_data:
            user_data[chat_id] = {}

        user_data[chat_id]['text'] = message.text  # Armazenar a mensagem para conversão
        bot.send_message(chat_id, "Escolha a voz para converter a mensagem em áudio:",
                         reply_markup=create_reply_keyboard())


# Inicia o bot
print("Bot iniciado com Sucesso!")
bot.polling()
