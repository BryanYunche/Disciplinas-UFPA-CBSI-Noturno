#Biblioteca para desenhar Bresenham sozinho
from AlgortitmosCG.circuloCG import Circulo

#Biblioteca para desenhar a grade
import AlgortitmosCG.TelaAnimacao as dt

#Inicia a malha instancianto ela em sua classe
malha = dt.MalhaQuadriculada()

#Importa Bresenhan
from AlgortitmosCG.RetaBresenham import Bresenham

#Importa a biblioteca tempo
import time

# Cores que podem ser utilizadas durante os testes
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#EXEMPLO DE BOLA QUICANDO


yBola = -10
centro = [0, yBola]

for i in range(3):
    if yBola == -10:
        for i in range(50):
            #Desenha o chão
            horizonte = Bresenham(-40, -17, 40, -17)
            dt.MalhaQuadriculada.pintar_quadrados(malha, VERDE, horizonte.saida)

            #Desenha a bola
            centro = [0, yBola]
            raio = 6

            #Recebe os pontos do circulo
            circulo = Circulo(centro, raio)
            circunferencia = circulo.saida

            #Pinta a malha
            dt.MalhaQuadriculada.pintar_quadrados(malha, AZUL, circunferencia)
            malha.atualizar_tela()
            time.sleep(0.04)

            #limpa a tela
            dt.MalhaQuadriculada.limpar_malha(malha)
            malha.atualizar_tela()

            yBola = yBola+1

            if yBola == 30:
                break
    if yBola == 30:
        for i in range(50):
            # Desenha o chão
            horizonte = Bresenham(-40, -17, 40, -17)
            dt.MalhaQuadriculada.pintar_quadrados(malha, VERDE, horizonte.saida)

            # Desenha a bola
            centro = [0, yBola]
            raio = 6

            # Recebe os pontos do circulo
            circulo = Circulo(centro, raio)
            circunferencia = circulo.saida

            # Pinta a malha
            dt.MalhaQuadriculada.pintar_quadrados(malha, VERMELHO, circunferencia)
            malha.atualizar_tela()
            time.sleep(0.04)

            # limpa a tela
            dt.MalhaQuadriculada.limpar_malha(malha)
            malha.atualizar_tela()

            yBola = yBola - 1

            if yBola == -10:
                break

