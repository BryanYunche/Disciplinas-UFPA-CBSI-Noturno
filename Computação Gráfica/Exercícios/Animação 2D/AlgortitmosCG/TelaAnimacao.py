import sys
import pygame

# Tamanho do quadrado na malha
TAMANHO_QUADRADO = 10

# Tamanho da tela
LARGURA_TELA = 1080
ALTURA_TELA = 720

# Cores que podem ser utilizadas na grade
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ROXO = (128, 0, 128)


class MalhaQuadriculada:
    def __init__(self):
        pygame.init()  # Inicializa o pygame
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))  # Cria a tela do jogo

        # Desenha a borda branca
        pygame.draw.rect(self.tela, AZUL, (0, 0, LARGURA_TELA, TAMANHO_QUADRADO))
        pygame.draw.rect(self.tela, AZUL, (0, ALTURA_TELA - TAMANHO_QUADRADO, LARGURA_TELA, TAMANHO_QUADRADO))
        pygame.draw.rect(self.tela, AZUL, (0, 0, TAMANHO_QUADRADO, ALTURA_TELA))
        pygame.draw.rect(self.tela, AZUL, (LARGURA_TELA - TAMANHO_QUADRADO, 0, TAMANHO_QUADRADO, ALTURA_TELA))

        # Desenha a cruz roxa que divide a malha em quadrantes
        pygame.draw.line(self.tela, ROXO, (LARGURA_TELA // 2, 0), (LARGURA_TELA // 2, ALTURA_TELA))
        pygame.draw.line(self.tela, ROXO, (0, ALTURA_TELA // 2), (LARGURA_TELA, ALTURA_TELA // 2))

        self.coordenadas_mouse = (0, 0)

    def desenhar_malha_tela(self):
        # Desenha as linhas horizontais da malha na tela
        for y in range(ALTURA_TELA // 2, -ALTURA_TELA // 2 - 1, -TAMANHO_QUADRADO):
            pygame.draw.line(self.tela, BRANCO, (0, y + ALTURA_TELA // 2), (LARGURA_TELA, y + ALTURA_TELA // 2))

        # Desenha as linhas verticais da malha na tela
        for x in range(-LARGURA_TELA // 2, LARGURA_TELA // 2 + 1, TAMANHO_QUADRADO):
            pygame.draw.line(self.tela, BRANCO, (x + LARGURA_TELA // 2, 0), (x + LARGURA_TELA // 2, ALTURA_TELA))

        # Desenha a cruz roxa que divide a malha em quadrantes
        pygame.draw.line(self.tela, ROXO, (LARGURA_TELA // 2, 0), (LARGURA_TELA // 2, ALTURA_TELA))
        pygame.draw.line(self.tela, ROXO, (0, ALTURA_TELA // 2), (LARGURA_TELA, ALTURA_TELA // 2))

    def pintar_quadrados(self, cor, coordenadas):
        # Pinta os quadrados da malha com a cor especificada
        for ponto in coordenadas:
            x, y = ponto
            x_pos = x * TAMANHO_QUADRADO + LARGURA_TELA // 2
            y_pos = -(y + 1) * TAMANHO_QUADRADO + ALTURA_TELA // 2
            pygame.draw.rect(self.tela, cor, (x_pos, y_pos, TAMANHO_QUADRADO, TAMANHO_QUADRADO))

    def limpar_malha(self):
        # Limpa a malha, preenchendo todos os quadrados com a cor de fundo
        self.tela.fill(PRETO)
        self.desenhar_malha_tela()

    def atualizar_tela(self):
        self.desenhar_malha_tela()
        pygame.display.update()


if __name__ == "__main__":
    malha = MalhaQuadriculada()

    # Mantém a janela aberta até que seja fechada pelo usuário
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        malha.atualizar_tela()
        pygame.time.delay(100)

    pygame.quit()
    sys.exit()

