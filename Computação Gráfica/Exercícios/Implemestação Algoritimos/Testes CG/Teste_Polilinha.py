#Biblioteca para desenhar a grade
import AlgortitmosCG.desenhaTela as dt

#Biblioteca para desenhar Polilinhas
from AlgortitmosCG.RetasPolilinhas import polilinha

# Cores que podem ser utilizadas durante os testes
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Inicia a malha instancianto ela em sua classe
malha = dt.MalhaQuadriculada()

#====================================================================

# #EXEMPLO DE POLILINHA 01 - SEM LIGAR O INICIO COM O FIM DA RETA
#
# # Exemplo de lista de coordenadas para colorir
# retasPolilinhas = polilinha(-42, -5, -31, -12, -27, -9, -21, -18, -14, -2)
#
# #Define a cor
# cor = VERDE
#
# #Pinta a malha
# malha.colorir_quadrados(cor, retasPolilinhas)

#====================================================================

# #EXEMPLO DE POLILINHA 02 - SEM LIGAR O INICIO COM O FIM DA RETA
#
# # Exemplo de lista de coordenadas para colorir
# retasPolilinhas = polilinha(-16, -15, -4, 18, 12, -14)
#
# #Define a cor
# cor = AZUL
#
# #Pinta a malha
# malha.colorir_quadrados(cor, retasPolilinhas)

#====================================================================

# #EXEMPLO DE POLILINHA 03 - SEM LIGAR O INICIO COM O FIM DA RETA
#
# # Exemplo de lista de coordenadas para colorir
# retasPolilinhas = polilinha(-35, -13, -27, 19, -3, 26, 19, 20, 29, -10, 9, -28)
#
# #Define a cor
# cor = VERMELHO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, retasPolilinhas)

#====================================================================

# #EXEMPLO DE POLILINHA 04 - LIGANDO O INICO NO FINAL
#
# # Exemplo de lista de coordenadas para colorir
# retasPolilinhas = polilinha(-42, -5, -31, -12, -27, -9, -21, -18, -14, -2, fechaPoligono=True)
#
# #Define a cor
# cor = VERDE
#
# #Pinta a malha
# malha.colorir_quadrados(cor, retasPolilinhas)

#====================================================================

# #EXEMPLO DE POLILINHA 05 - SEM LIGAR O INICIO COM O FIM DA RETA
#
# # Exemplo de lista de coordenadas para colorir
# retasPolilinhas = polilinha(-16, -15, -4, 18, 12, -14, fechaPoligono=True)
#
# #Define a cor
# cor = AZUL
#
# #Pinta a malha
# malha.colorir_quadrados(cor, retasPolilinhas)

#====================================================================

# #EXEMPLO DE POLILINHA 06 - SEM LIGAR O INICIO COM O FIM DA RETA
#
# # Exemplo de lista de coordenadas para colorir
# retasPolilinhas = polilinha(-35, -13, -27, 19, -3, 26, 19, 20, 29, -10, 9, -28, fechaPoligono=True)
#
# #Define a cor
# cor = VERMELHO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, retasPolilinhas)

#====================================================================

#Executa a malha para os testes
malha.executar()