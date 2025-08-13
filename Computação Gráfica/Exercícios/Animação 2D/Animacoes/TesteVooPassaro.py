#Biblioteca para desenhar a grade
import AlgortitmosCG.TelaAnimacao as dt

#Biblioteca para desenhar Bresenham sozinho
from AlgortitmosCG.CurvasCasteljau import curvas

#Inicia a malha instancianto ela em sua classe
malha = dt.MalhaQuadriculada()

#Importa a biblioteca tempo
import time

# Cores que podem ser utilizadas durante os testes
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ROXO = (128, 0, 128)

y = 20
for i in range(2):
    if y == 20:
        for i in range(50):
            y = y-1

            linhaBezier = [[-40, y], [-15, 0], [-1, 0], [0, 0], [15, 0], [40, y]]

            # Curva 01 de bezier
            curva = curvas(20, linhaBezier)
            dt.MalhaQuadriculada.pintar_quadrados(malha, AZUL, curva)
            malha.atualizar_tela()
            time.sleep(0.04)

            dt.MalhaQuadriculada.limpar_malha(malha)
            malha.atualizar_tela()
            if y == -20:
                break
    if y == -20:
        for i in range(50):
            y = y+1

            linhaBezier = [[-40, y], [-15, 0], [-25, 0], [-1, 0], [0, 0], [25, 0], [15, 0], [40, y]]

            # Curva 01 de bezier
            curva = curvas(20, linhaBezier)
            dt.MalhaQuadriculada.pintar_quadrados(malha, VERDE, curva)
            malha.atualizar_tela()
            time.sleep(0.04)

            dt.MalhaQuadriculada.limpar_malha(malha)
            malha.atualizar_tela()
            if y == 20:
                break
