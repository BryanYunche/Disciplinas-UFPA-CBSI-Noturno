import telebot
from telebot import types
from google.cloud import texttospeech
import uuid
import os

# Token do seu bot (obtenha em https://core.telegram.org/bots:new)
BOT_TOKEN =('7617534366:AAE7kGQuG6sGwZIT6tEMwsMXSDyX3B2eWk8')

# Caminho para o arquivo JSON da chave de autenticação do Google Cloud
GOOGLE_CLOUD_CREDENTIALS_JSON = r"chavesAPI\\apiKey.json"

bot = telebot.TeleBot(BOT_TOKEN)

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


# Função para converter texto em áudio usando Google Cloud Text-to-Speech
def convert_text_to_speech_google(text, voice_type, chat_id):
    # Inicializar o cliente de síntese de fala usando o arquivo da chave JSON
    client = texttospeech.TextToSpeechClient.from_service_account_file(GOOGLE_CLOUD_CREDENTIALS_JSON)

    # Definindo a configuração de síntese de voz
    if voice_type == 'voz masculina':
        voice = texttospeech.VoiceSelectionParams(
            language_code="pt-BR",
            ssml_gender=texttospeech.SsmlVoiceGender.MALE
        )
    else:
        voice = texttospeech.VoiceSelectionParams(
            language_code="pt-BR",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
        )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Requisição de síntese de voz
    synthesis_input = texttospeech.SynthesisInput(text=text)

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Gera um nome de arquivo único
    filename = f"audio_{uuid.uuid4()}.mp3"

    # Salva o áudio gerado no arquivo
    with open(filename, "wb") as out:
        out.write(response.audio_content)

    # Enviar o áudio para o usuário
    with open(filename, 'rb') as audio:
        bot.send_audio(chat_id, audio)

    # Remove o arquivo temporário
    if os.path.exists(filename):
        os.remove(filename)


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
                voice_type = 'voz masculina' if user_data[chat_id]['voice'] == 'voz masculina' else 'voz feminina'
                convert_text_to_speech_google(user_data[chat_id]['text'], voice_type, chat_id)
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
