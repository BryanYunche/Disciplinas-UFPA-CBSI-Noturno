#Biblioteca para desenhar a grade
import AlgortitmosCG.desenhaTela as dt

#Biblioteca para desenhar Bresenham sozinho
from AlgortitmosCG.circuloCG import Circulo

# Cores que podem ser utilizadas durante os testes
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Inicia a malha instancianto ela em sua classe
malha = dt.MalhaQuadriculada()

#====================================================================

# #EXEMPLO DE CIRCULO 01(0.25pts)
#
# #Define os argumentos
# centro = [0, 0]
# raio = 10
#
# #Recebe os pontos do circulo
# circulo = Circulo(centro, raio)
# circunferencia = circulo.saida
#
# #Define a cor
# cor = VERDE
#
# #Pinta a malha
# malha.colorir_quadrados(cor, circunferencia)

#====================================================================

# #EXEMPLO DE CIRCULO 02(0.25pts)
#
# #Define os argumentos
# centro = [-10, 3]
# raio = 20
#
# #Recebe os pontos do circulo
# circulo = Circulo(centro, raio)
# circunferencia = circulo.saida
#
# #Define a cor
# cor = VERMELHO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, circunferencia)

#====================================================================

# #EXEMPLO DE CIRCULO 03(0.25pts)
#
# #Define os argumentos
# centro = [-25, 13]
# raio = 5
#
# #Recebe os pontos do circulo
# circulo = Circulo(centro, raio)
# circunferencia = circulo.saida
#
# #Define a cor
# cor = BRANCO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, circunferencia)

#====================================================================

# #EXEMPLO DE CIRCULO 04(0.25pts)
#
# #Define os argumentos
# centro = [-13, -9]
# raio = 7
#
# #Recebe os pontos do circulo
# circulo = Circulo(centro, raio)
# circunferencia = circulo.saida
#
# #Define a cor
# cor = VERDE
#
# #Pinta a malha
# malha.colorir_quadrados(cor, circunferencia)

#====================================================================

#Executa a malha para os testes
malha.executar()