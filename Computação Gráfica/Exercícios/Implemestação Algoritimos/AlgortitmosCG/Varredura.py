import sys

class Rasterizacao:
    def __init__(self, entrada):
        self.entrada = entrada  # Lista de pontos de entrada
        self.saida = []  # Lista de pontos de saída

# Classe que representa um ponto crítico (ponto de interseção)
class PontoCritico:
    def __init__(self, index, dir, x_interseccao, inv_slope):
        self.index = index  # Índice do ponto crítico no polígono
        self.dir = dir  # Direção do ponto crítico (1: cima para baixo, -1: baixo para cima)
        self.x_interseccao = x_interseccao  # Coordenada x da interseção com a linha de varredura
        self.inv_slope = inv_slope  # Inverso do coeficiente angular da reta que cruza o ponto crítico

    def __lt__(self, outro):
        return self.x_interseccao < outro.x_interseccao

# Classe que realiza a técnica de varredura em um polígono
class Varredura(Rasterizacao):
    def __init__(self, poligono):
        super().__init__(poligono)

        ymax = -sys.maxsize  # Valor máximo para a coordenada y
        ymin = sys.maxsize  # Valor mínimo para a coordenada y

        pts_criticos = []  # Lista de pontos críticos

        # Encontra os pontos críticos do polígono
        for i in range(len(poligono)):
            if poligono[i][1] < ymin:
                ymin = poligono[i][1]  # Atualiza o valor mínimo de y
            if poligono[i][1] > ymax:
                ymax = poligono[i][1]  # Atualiza o valor máximo de y

            ponto_aux = poligono[(i+1)%len(poligono)]
            # Verifica se o ponto atual é um ponto crítico em relação aos seus pontos adjacentes
            if poligono[i][1] < ponto_aux[1]:
                # Calcula o coeficiente angular inverso da reta que cruza o ponto crítico
                inv_slope = (ponto_aux[0] - poligono[i][0]) / (ponto_aux[1] - poligono[i][1])
                c = PontoCritico(i, dir=1, x_interseccao=poligono[i][0], inv_slope=inv_slope)
                pts_criticos.append(c)

            ponto_aux = poligono[(i-1)]
            if poligono[i][1] < ponto_aux[1]:
                inv_slope = (ponto_aux[0] - poligono[i][0]) / (ponto_aux[1] - poligono[i][1])
                c = PontoCritico(i, dir=-1, x_interseccao=poligono[i][0], inv_slope=inv_slope)
                pts_criticos.append(c)

        ativos = []  # Lista de pontos críticos ativos

        # Varre verticalmente as linhas do polígono
        for y in range(ymin, ymax+1):
            for ponto in ativos:
                ponto.x_interseccao += ponto.inv_slope  # Atualiza a coordenada x da interseção com a linha de varredura

            for pt in pts_criticos:
                if poligono[pt.index][1] == y:
                    ativos.append(pt)  # Adiciona o ponto crítico à lista de pontos críticos ativos

            # Remove os pontos críticos que não estão mais ativos
            for i in range(len(ativos)-1, -1, -1):
                c = ativos[i]
                p_max = poligono[(c.index + c.dir + len(poligono))%len(poligono)]
                if p_max[1] == y:
                    ativos.pop(i)

            ativos.sort()  # Ordena os pontos críticos ativos por coordenada x de interseção

            # Desenha as linhas horizontais entre os pares de pontos críticos ativos
            for i in range(0, len(ativos), 2):
                xmin = round(ativos[i].x_interseccao)  # Coordenada x do ponto de início da linha
                xmax = round(ativos[i+1].x_interseccao)  # Coordenada x do ponto de fim da linha
                for x in range(xmin, xmax):
                    self.saida.append([x, y])  # Adiciona o ponto (x, y) à lista de pontos de saída
