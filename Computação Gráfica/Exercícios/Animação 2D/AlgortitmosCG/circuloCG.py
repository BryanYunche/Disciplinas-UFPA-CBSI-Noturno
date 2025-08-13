class Circulo:
    def __init__(self, centro, raio):
        # Armazena as coordenadas do centro e arredonda o raio para o valor inteiro mais próximo
        self.centro = centro
        self.raio = round(raio)

        # Lista vazia para armazenar os pontos finais do círculo
        self.saida = []

        # Chama o método ponto_medio para calcular os pontos do círculo
        self.ponto_medio()

    def ponto_medio(self):
        # Inicializa as variáveis x, y e erro
        x = 0
        y = self.raio
        erro = -self.raio

        # Chama o método printOctantes para adicionar os primeiros pontos aos octantes correspondentes
        self.printOctantes(x, y)

        # Loop para calcular os pontos restantes do círculo
        while x <= y:
            # Calcula o próximo valor do erro
            erro = self.proximoErro(x, y, erro)

            # Incrementa x e verifica se o erro é maior ou igual a 0
            x += 1
            if erro >= 0:
                # Calcula o erro final e decrementa y
                erro = self.erroFinal(x, y, erro)
                y -= 1

            # Chama o método printOctantes para adicionar os pontos aos octantes correspondentes
            self.printOctantes(x, y)

    def proximoErro(self, x, y, erro):
        # Calcula o próximo valor do erro
        return erro + 2 * x + 1

    def erroFinal(self, x, y, erro):
        # Calcula o erro final
        return erro - 2 * y + 2

    def printOctantes(self, x, y):
        # Adiciona os pontos aos octantes correspondentes, considerando o centro do círculo
        self.saida.append([x + self.centro[0], y + self.centro[1]])
        self.saida.append([y + self.centro[0], x + self.centro[1]])
        self.saida.append([y + self.centro[0], -x + self.centro[1]])
        self.saida.append([x + self.centro[0], -y + self.centro[1]])
        self.saida.append([-x + self.centro[0], -y + self.centro[1]])
        self.saida.append([-y + self.centro[0], -x + self.centro[1]])
        self.saida.append([-y + self.centro[0], x + self.centro[1]])
        self.saida.append([-x + self.centro[0], y + self.centro[1]])
