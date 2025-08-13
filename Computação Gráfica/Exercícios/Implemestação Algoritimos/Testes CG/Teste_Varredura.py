#Biblioteca para desenhar a grade
import AlgortitmosCG.desenhaTela as dt

#Biblioteca para desenhar Polilinhas
from AlgortitmosCG.RetasPolilinhas import polilinha

#Biblioteca para preencher por varredura
from AlgortitmosCG.Varredura import Varredura

# Cores que podem ser utilizadas durante os testes
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Inicia a malha instancianto ela em sua classe
malha = dt.MalhaQuadriculada()

#====================================================================
#EXEMPLO DE PREENCHIMENTO POR VARREDURA 01

# # Exemplo de lista de coordenadas para colorir
# poligono = [(-8, -8), (8, 8), (-16, 16)]
# poligonoDesenhado = Varredura(poligono)
#
# #Define a cor da borda
# cor = VERDE
#
# #Pinta a malha
# malha.colorir_quadrados(cor, poligonoDesenhado.saida)

#====================================================================

#EXEMPLO DE PREENCHIMENTO POR VARREDURA 02

# # Exemplo de lista de coordenadas para colorir
# poligono = [(-42, -5), (-31, -12), (-27, -9), (-21, -18), (-14, -2)]
# poligonoDesenhado = Varredura(poligono)
#
# #Define a cor da borda
# cor = BRANCO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, poligonoDesenhado.saida)

#====================================================================

# #EXEMPLO DE PREENCHIMENTO POR VARREDURA 03
#
# # Exemplo de lista de coordenadas para colorir
# poligono = [(-16, -15), (-4, 18), (12, -14)]
# poligonoDesenhado = Varredura(poligono)
#
# #Define a cor da borda
# cor = AZUL
#
# #Pinta a malha
# malha.colorir_quadrados(cor, poligonoDesenhado.saida)

#====================================================================

# #EXEMPLO DE PREENCHIMENTO POR VARREDURA 04
#
# # Exemplo de lista de coordenadas para colorir
# poligono = [(-35, -13), (-27, 19), (-3, 26), (19, 20), (29, -10), (9, -28)]
# poligonoDesenhado = Varredura(poligono)
#
# #Define a cor da borda
# cor = VERMELHO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, poligonoDesenhado.saida)

#====================================================================

#Executa a malha para os testes
malha.executar()