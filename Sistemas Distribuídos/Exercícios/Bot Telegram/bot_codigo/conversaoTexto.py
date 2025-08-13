import os
from google.cloud import texttospeech, language_v1

# Define a classe ClienteTextoAudio
class ClienteTextoAudio:
    def __init__(self, chave_google, texto_usuario, id_usuario):
        """
        Inicializa a classe com as credenciais do Google Cloud, o texto a ser convertido e o ID do usuário.
        """
        self.chave_google = chave_google
        self.texto_usuario = texto_usuario
        self.id_usuario = id_usuario

        # Define a variável de ambiente para autenticação com a chave do Google Cloud
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.chave_google

        # Cria os clientes das APIs para evitar recriação desnecessária
        self.language_client = language_v1.LanguageServiceClient()
        self.tts_client = texttospeech.TextToSpeechClient()

    def analisar_texto(self):
        """
        Analisa o sentimento do texto usando a API de Natural Language do Google Cloud.
        """
        document = language_v1.Document(content=self.texto_usuario, type_=language_v1.Document.Type.PLAIN_TEXT)

        try:
            # Analisa o sentimento do documento
            sentiment = self.language_client.analyze_sentiment(request={"document": document}).document_sentiment
            return sentiment
        except Exception as e:
            print(f"Erro ao analisar o texto: {e}")
            return None

    def converte_texto_audio(self):
        """
        Converte o texto em áudio usando a API Text-to-Speech do Google Cloud, ajustando os parâmetros com base no sentimento.
        """
        sentiment = self.analisar_texto()

        # Ajusta parâmetros de voz baseados no sentimento, se o sentimento for nulo, usa valores padrão
        speaking_rate = 1.0
        pitch = 0.0
        if sentiment:
            # Calcula a taxa de fala, limitando a 1.2 para evitar velocidade excessiva
            speaking_rate = min(1.0 + (sentiment.score * 0.5), 1.2)
            pitch = sentiment.score * 2.0

        synthesis_input = texttospeech.SynthesisInput(text=self.texto_usuario)
        voice = texttospeech.VoiceSelectionParams(
            language_code="pt-BR", 
            ssml_gender=texttospeech.SsmlVoiceGender.MALE
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3, 
            speaking_rate=speaking_rate,
            pitch=pitch,
            volume_gain_db=0.0
        )

        try:
            response = self.tts_client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )
            return response.audio_content
        except Exception as e:
            print(f"Erro ao converter texto para áudio: {e}")
            return None

    def salva_audio(self):
        """
        Salva o áudio gerado em um arquivo MP3 na pasta 'audios_gerados'.
        """
        audio_mp3 = self.converte_texto_audio()

        if audio_mp3:
            dir_atual = os.path.dirname(__file__)
            caminho_pasta = os.path.join(dir_atual, "..", "audios_gerados")
            os.makedirs(caminho_pasta, exist_ok=True)

            caminho_arquivo = os.path.join(caminho_pasta, f'{self.id_usuario}_Audio.mp3')

            try:
                with open(caminho_arquivo, "wb") as audio_file:
                    audio_file.write(audio_mp3)
                print(f"Áudio salvo em: {caminho_arquivo}")
                return caminho_arquivo
            except Exception as e:
                print(f"Erro ao salvar o arquivo de áudio: {e}")
                return None
        else:
            print("Não foi possível gerar o áudio.")
            return None
