from AlgortitmosCG.RetaBresenham import Bresenham
from AlgortitmosCG.RetasPolilinhas import polilinha
from math import sin, cos, radians
import numpy as np

# Classe base para as operações de rasterização
class Rasterizacao:
    def __init__(self, entrada):
        self.entrada = entrada
        self.saida = []


# Classe que representa as transformações geométricas
class Transformacao(Rasterizacao):
    def __init__(self, entrada):
        super().__init__(entrada)
        self.saida = entrada

    def translar(self, trans_x, trans_y):
        self.saida = []
        for ponto in self.entrada:
            ponto[0] += trans_x  # Incrementa a coordenada x do ponto pela quantidade de translação em x
            ponto[1] += trans_y  # Incrementa a coordenada y do ponto pela quantidade de translação em y
            self.saida.append(ponto)  # Adiciona o ponto à lista de saída

    def escalar(self, esc_x, esc_y):
        self.saida = []
        for ponto in self.entrada:
            ponto[0] *= esc_x  # Multiplica a coordenada x do ponto pelo fator de escala em x
            ponto[1] *= esc_y  # Multiplica a coordenada y do ponto pelo fator de escala em y
            self.saida.append(ponto)  # Adiciona o ponto à lista de saída
        self.saida.append(self.saida[0])  # Adiciona o primeiro ponto novamente para fechar a polilinha

        # Desempacota os pontos da lista para a função de polilinha
        pontos_desempacotados = [coord for ponto in self.saida for coord in ponto]
        self.saida = polilinha(*pontos_desempacotados)  # Gera a polilinha com os pontos desempacotados

    def rotacionar(self, pivo, angulo):
        self.saida = []

        # Realiza a translação para o pivô ser a origem
        trans_x = 0 - pivo[0]
        trans_y = 0 - pivo[1]
        translacao = Transformacao(self.entrada)
        translacao.translar(trans_x, trans_y)
        self.entrada = translacao.saida

        # Converte o ângulo para radianos
        angulo_rad = radians(angulo)

        # Matriz de rotação
        matriz_rotacao = [[cos(angulo_rad), -sin(angulo_rad)],
                          [sin(angulo_rad), cos(angulo_rad)]]

        # Aplica a rotação a cada ponto
        for ponto in self.entrada:
            self.saida.append([round(x) for x in np.dot(matriz_rotacao, ponto)])

        # Realiza a translação inversa para voltar à posição original
        translacao = Transformacao(self.saida)
        translacao.translar(-trans_x, -trans_y)
        self.saida = translacao.saida


# Classe que representa uma polilinha
class Polilinha(Rasterizacao):
    def __init__(self, pontos: list, fechar=False):
        super().__init__(pontos)

        # Verifica se a polilinha deve ser fechada
        if fechar:
            pontos.append(pontos[0])

        # Gera as retas entre os pontos da polilinha usando o algoritmo de Bresenham
        for x in range(len(pontos) - 1):
            linha = Bresenham(pontos[x][0], pontos[x][1], pontos[x + 1][0], pontos[x + 1][1])

            # Adiciona os pontos da linha à lista de saída
            for ponto in linha.saida:
                self.saida.append(ponto)

