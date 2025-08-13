#Biblioteca para desenhar a grade
import AlgortitmosCG.TelaAnimacao as dt

#Biblioteca para desenhar Bresenham sozinho
from AlgortitmosCG.CurvasCasteljau import curvas

#Biblioteca para desenhar Bresenham sozinho
from AlgortitmosCG.circuloCG import Circulo

#Importa a biblioteca tempo
import time

#Inicia a malha instancianto ela em sua classe
malha = dt.MalhaQuadriculada()

# Cores que podem ser utilizadas durante os testes
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

linhaBezier = [[-35, 0], [-25, -25], [-15, -15], [15, 15], [25, 25], [35, 0]]

# Curva 01 de bezier
curva = curvas(20, linhaBezier)

for pontoCont in curva:

    # Desenha a bola
    centro = pontoCont
    raio = 6

    # Recebe os pontos do circulo
    circulo = Circulo(centro, raio)
    circunferencia = circulo.saida

    # Pinta a malha
    dt.MalhaQuadriculada.pintar_quadrados(malha, AZUL, circunferencia)
    malha.atualizar_tela()
    time.sleep(0.09)

    # limpa a tela
    dt.MalhaQuadriculada.limpar_malha(malha)
    malha.atualizar_tela()













