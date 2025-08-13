#Biblioteca para desenhar a grade
import AlgortitmosCG.desenhaTela as dt

#Biblioteca para desenhar Bresenham sozinho
from AlgortitmosCG.RetaBresenham import Bresenham

# Cores que podem ser utilizadas durante os testes
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Inicia a malha instancianto ela em sua classe
malha = dt.MalhaQuadriculada()

#====================================================================

# #EXEMPLO DE BRESENHAM 01 (0.25pts)
#
# # Exemplo de lista de coordenadas para colorir
# bresenham = Bresenham(1, 1, 10, 13)
# reta = bresenham.saida
#
# ##Define a cor
# cor = VERDE
#
# #Pinta a malha
# malha.colorir_quadrados(cor, reta)

#====================================================================

# #EXEMPLO DE BRESENHAM 02 (0.25pts)
#
# # Exemplo de lista de coordenadas para colorir
# bresenham = Bresenham(-13, -9, 10, 13)
# reta = bresenham.saida
#
# ##Define a cor
# cor = BRANCO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, reta)

#====================================================================

# #EXEMPLO DE BRESENHAM 03 (0.25pts)
#
# # Exemplo de lista de coordenadas para colorir
# bresenham = Bresenham(20, 15, -17, -5)
# reta = bresenham.saida
#
# ##Define a cor
# cor = VERMELHO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, reta)

#====================================================================

# #EXEMPLO DE BRESENHAM 04 (0.25pts)
#
# # Exemplo de lista de coordenadas para colorir
# bresenham = Bresenham(-20, 15, 17, -5)
# reta = bresenham.saida
#
# ##Define a cor
# cor = AZUL
#
# #Pinta a malha
# malha.colorir_quadrados(cor, reta)

#====================================================================

#Executa a malha para os testes
malha.executar()


