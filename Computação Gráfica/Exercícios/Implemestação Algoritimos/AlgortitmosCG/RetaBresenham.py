class Bresenham:
    def __init__(self, x1, y1, x2, y2):
        # Coordenadas do ponto inicial e final da linha
        self.xInicial = x1
        self.yInicial = y1
        self.xFinal = x2
        self.yFinal = y2

        # Lista para armazenar os pontos finais da linha
        self.pontosFinais = []

        # Variáveis de controle para possíveis reflexões ou trocas de coordenadas
        self.trocaX = False
        self.trocaY = False
        self.trocaXY = False

        # Verifica se os pontos inicial e final são iguais
        if (x1, y1) == (x2, y2):
            # Se forem iguais, apenas adiciona o ponto inicial à lista de pontos finais
            self.pontosFinais = [[x1, y1]]
            self.saida = self.pontosFinais
            return

        # Determina o octante em que a linha está
        self.octante()

        # Variáveis auxiliares para o algoritmo de Bresenham
        auxX = self.xInicial
        auxY = self.yInicial

        # Diferença entre as coordenadas x e y
        deltaX = self.xFinal - self.xInicial
        deltaY = self.yFinal - self.yInicial

        # Coeficiente angular da reta
        m = deltaY / deltaX
        erro = m - (1 / 2)

        # Adiciona o ponto inicial à lista de pontos finais
        self.pontosFinais.append([auxX, auxY])

        # Algoritmo de Bresenham para traçar a linha
        while auxX < self.xFinal:
            if erro >= 0:
                auxY += 1
                erro -= 1
            auxX += 1
            erro += m
            self.pontosFinais.append([auxX, auxY])

        # Aplica reflexões ou trocas de coordenadas, se necessário
        self.reflexao(self.pontosFinais)

        # Define a saída como os pontos finais da linha
        self.saida = self.pontosFinais

    def octante(self):
        # Calcula a diferença entre as coordenadas x e y
        deltaX = self.xFinal - self.xInicial
        deltaY = self.yFinal - self.yInicial

        # Calcula o coeficiente angular da reta
        if deltaX != 0:
            m = deltaY / deltaX
        else:
            m = 2

        # Verifica se a reta está em um octante que requer reflexão ou troca de coordenadas
        if m > 1 or m < -1:
            self.xInicial, self.yInicial = self.yInicial, self.xInicial
            self.xFinal, self.yFinal = self.yFinal, self.xFinal
            self.trocaXY = True

        # Verifica se é necessário inverter as coordenadas x
        if self.xInicial > self.xFinal:
            self.xInicial = -self.xInicial
            self.xFinal = -self.xFinal
            self.trocaX = True

        # Verifica se é necessário inverter as coordenadas y
        if self.yInicial > self.yFinal:
            self.yInicial = -self.yInicial
            self.yFinal = -self.yFinal
            self.trocaY = True

    def reflexao(self, pts):
        # Aplica reflexão nas coordenadas y, se necessário
        if self.trocaY:
            for ponto in pts:
                ponto[1] = -ponto[1]

        # Aplica reflexão nas coordenadas x, se necessário
        if self.trocaX:
            for ponto in pts:
                ponto[0] = -ponto[0]

        # Aplica reflexão nas coordenadas x e y, se necessário
        if self.trocaXY:
            for ponto in pts:
                ponto[0], ponto[1] = ponto[1], ponto[0]

        # Atualiza a lista de pontos finais com as reflexões aplicadas
        self.pontosFinais = pts
