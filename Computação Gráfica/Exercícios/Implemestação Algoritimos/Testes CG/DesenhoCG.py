
#Biblioteca para desenhar Bresenham sozinho
from AlgortitmosCG.circuloCG import Circulo

#Biblioteca para preencher por varredura
from AlgortitmosCG.Varredura import Varredura

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
#OLHO 01

#Define os argumentos
centro = [-20, 16]
raio = 10

#Recebe os pontos do circulo
circulo = Circulo(centro, raio)
circunferencia = circulo.saida

#Define a cor
cor = VERDE

#Pinta a malha
malha.colorir_quadrados(cor, circunferencia)

#====================================================================
#OLHO 02

#Define os argumentos
centro = [20, 16]
raio = 10

#Recebe os pontos do circulo
circulo = Circulo(centro, raio)
circunferencia = circulo.saida

#Define a cor
cor = VERDE

#Pinta a malha
malha.colorir_quadrados(cor, circunferencia)

#====================================================================
#PUPILA 01

# Exemplo de lista de coordenadas para colorir
poligono = [(-22, 17), (-15, 17), (-15, 11), (-22, 11)]
poligonoDesenhado = Varredura(poligono)

#Define a cor da borda
cor = VERMELHO

#Pinta a malha
malha.colorir_quadrados(cor, poligonoDesenhado.saida)

#====================================================================
#PUPILA 02

# Exemplo de lista de coordenadas para colorir
poligono = [(18, 17), (25, 17), (25, 11), (18, 11)]
poligonoDesenhado = Varredura(poligono)

#Define a cor da borda
cor = VERMELHO

#Pinta a malha
malha.colorir_quadrados(cor, poligonoDesenhado.saida)

#====================================================================
#SORRISO

#Define os pontos de controle da curva de bezier
curva = curvas(200, [[-30, -3], [-15, -25],[-25, -20], [25, -20], [15, -25], [30, -3]])

curvaDeBezier = curva

#Define a cor
cor = VERMELHO

#Pinta a malha
malha.colorir_quadrados(cor, curvaDeBezier)

#====================================================================

#Executa a malha para os testes
malha.executar()