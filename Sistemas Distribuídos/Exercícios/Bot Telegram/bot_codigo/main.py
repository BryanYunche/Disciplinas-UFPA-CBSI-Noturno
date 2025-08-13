from conversaoTexto import ClienteTextoAudio

# Exemplo de uso da classe ClienteTextoAudio

# Caminho para o arquivo JSON com a chave da API do Google Cloud
chave_google = r"C:\\Users\\Bryan\\Documents\\Primeiro_Semestre_2024\\Sistemas_Distribuidos_UFPA\\Trabalhos_Praticos\\Trabalho_03\\chavesAPI\\apiKey.json"

# Texto que será convertido em áudio
texto_usuario = '''E conversamos toda a noite, enquanto
A Via Láctea, como um pálio aberto,
Cintila. E, ao vir do sol, saudoso e em pranto,
Inda as procuro pelo céu deserto.'''

# ID do usuário para nomear o arquivo de áudio gerado
iDUserTelegram = "Bryan"

# Cria uma instância da classe ClienteTextoAudio com as credenciais e texto fornecidos
cliente = ClienteTextoAudio(chave_google, texto_usuario, iDUserTelegram)

# Converte o texto em áudio e salva o arquivo
cliente.salva_audio()




