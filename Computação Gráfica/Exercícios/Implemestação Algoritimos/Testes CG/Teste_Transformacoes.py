#Biblioteca para desenhar a grade
import AlgortitmosCG.desenhaTela as dt

#Bilioteca de Transformações
import AlgortitmosCG.transforma as trans

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
#FORMA ORIGINAL QUE SERÁ MODIFICADA

# Exemplo de lista de coordenadas para colorir
retasPolilinhas = polilinha(-7, 4, 7, 4, 7, -6, -7, -6, fechaPoligono=True)

#Define a cor
cor = VERDE

#Pinta a malha
malha.colorir_quadrados(cor, retasPolilinhas)

#====================================================================

# #EXEMPLO DE TRANSFORMAÇÃO DE TRANSLAÇÃO OU DESLOCAMENTO
#
# #Faz com que o poligono seja instanciado como um objeto que pode sofrer transformações
# objetoDeTransfomacao = trans.Transformacao(entrada=retasPolilinhas)
#
# objetoDeTransfomacao.translar(20, 20) #(0.25pts)
#
# #Define a cor
# cor = AZUL
#
# #Pinta a malha
# malha.colorir_quadrados(cor, objetoDeTransfomacao.saida)

#====================================================================

# #EXEMPLO DE TRANSFORMAÇÃO ESCALAR
#
# #Faz com que o poligono seja instanciado como um objeto que pode sofrer transformações
# objetoDeTransfomacao = trans.Transformacao(entrada=retasPolilinhas)
#
# objetoDeTransfomacao.escalar(5, 5) #(0.25pts)
# #objetoDeTransfomacao.rotacionar([0, 0], 45)
#
# #Define a cor
# cor = VERMELHO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, objetoDeTransfomacao.saida)

#====================================================================

#EXEMPLO DE TRANSFORMAÇÃO POR ROTAÇÃO

#Faz com que o poligono seja instanciado como um objeto que pode sofrer transformações
objetoDeTransfomacao = trans.Transformacao(entrada=retasPolilinhas)

#----------------------- ROTAÇÃO 90----------------------------------

# #Define o ponto pivo e a rotação como argumento
# objetoDeTransfomacao.rotacionar([7, -6], 90)
#
# #Define a cor
# cor = VERMELHO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, objetoDeTransfomacao.saida)
#
#  #----------------------- ROTAÇÃO 180----------------------------------
#
# #Define o ponto pivo e a rotação como argumento
# objetoDeTransfomacao.rotacionar([7, -6], 180)
#
# #Define a cor
# cor = VERMELHO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, objetoDeTransfomacao.saida)
#
# #----------------------- ROTAÇÃO 270----------------------------------
#
# #Define o ponto pivo e a rotação como argumento
# objetoDeTransfomacao.rotacionar([7, -6], 270)
#
# #Define a cor
# cor = VERMELHO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, objetoDeTransfomacao.saida)
#
# #----------------------- ROTAÇÃO 360----------------------------------
#
# #Define o ponto pivo e a rotação como argumento
# objetoDeTransfomacao.rotacionar([7, -6], 360)
#
# #Define a cor
# cor = VERMELHO
#
# #Pinta a malha
# malha.colorir_quadrados(cor, objetoDeTransfomacao.saida)

#====================================================================

#Executa a malha para os testes
malha.executar()

