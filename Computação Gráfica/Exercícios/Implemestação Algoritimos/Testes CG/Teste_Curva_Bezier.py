#Biblioteca para desenhar a grade
import AlgortitmosCG.desenhaTela as dt

#Biblioteca para desenhar Bresenham sozinho
from AlgortitmosCG.CurvasCasteljau import curvas

# Cores que podem ser utilizadas durante os testes
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Inicia a malha instancianto ela em sua classe
malha = dt.MalhaQuadriculada()

#====================================================================

# #EXEMPLO DE CURVA DE BEZIER 01
#
# #Define os pontos de controle da curva de bezier
# curva = curvas(20, [[0, 0], [5, -5], [15, -5], [20, 20]])
#
# curvaDeBezier = curva
#
# #Define a cor
# cor = VERDE
#
# #Pinta a malha
# malha.colorir_quadrados(cor, curvaDeBezier)

#====================================================================

# #EXEMPLO DE CURVA DE BEZIER 02
#
# #Define os pontos de controle da curva de bezier
# curva = curvas(20, [[-25, -9], [-20, 10], [25, 10], [25, -9]])
#
# curvaDeBezier = curva
#
# #Define a cor
# cor = AZUL
#
# #Pinta a malha
# malha.colorir_quadrados(cor, curvaDeBezier)

#====================================================================

# #EXEMPLO DE CURVA DE BEZIER 03
#
# #Define os pontos de controle da curva de bezier
# curva = curvas(20, [[-30, -3], [-20, -20], [25, -20], [30, -3]])
#
# curvaDeBezier = curva
#
# #Define a cor
# cor = VERMELHO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, curvaDeBezier)

#====================================================================

# #EXEMPLO DE CURVA DE BEZIER 04
#
# #Define os pontos de controle da curva de bezier
# curva = curvas(200, [[-30, -3], [-15, -25],[-25, -20], [25, -20], [15, -25], [30, -3]])
#
# curvaDeBezier = curva
#
# #Define a cor
# cor = BRANCO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, curvaDeBezier)

#====================================================================

#Executa a malha para os testes
malha.executar()