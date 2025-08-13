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
        # Inicializa a tela do pygame
        self.tela = self.iniciar_tela()

    def iniciar_tela(self):
        # Inicializa a tela do pygame com o tamanho especificado
        pygame.init()
        tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

        # Desenha a borda branca
        pygame.draw.rect(tela, AZUL, (0, 0, LARGURA_TELA, TAMANHO_QUADRADO))
        pygame.draw.rect(tela, AZUL, (0, ALTURA_TELA - TAMANHO_QUADRADO, LARGURA_TELA, TAMANHO_QUADRADO))
        pygame.draw.rect(tela, AZUL, (0, 0, TAMANHO_QUADRADO, ALTURA_TELA))
        pygame.draw.rect(tela, AZUL, (LARGURA_TELA - TAMANHO_QUADRADO, 0, TAMANHO_QUADRADO, ALTURA_TELA))

        # Desenha a cruz roxa que divide a malha em quadrantes
        pygame.draw.line(tela, ROXO, (LARGURA_TELA // 2, 0), (LARGURA_TELA // 2, ALTURA_TELA))
        pygame.draw.line(tela, ROXO, (0, ALTURA_TELA // 2), (LARGURA_TELA, ALTURA_TELA // 2))

        return tela

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

    def colorir_quadrados(self, cor, coordenadas):
        # Pinta os quadrados da malha com a cor especificada
        for ponto in coordenadas:
            x, y = ponto
            x_pos = x * TAMANHO_QUADRADO + LARGURA_TELA // 2
            y_pos = -(y + 1) * TAMANHO_QUADRADO + ALTURA_TELA // 2
            pygame.draw.rect(self.tela, cor, (x_pos, y_pos, TAMANHO_QUADRADO, TAMANHO_QUADRADO))

    def executar(self):
        coordenadas_mouse = (0, 0)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    # Obtém as coordenadas do mouse e converte para as coordenadas da malha
                    x, y = event.pos
                    x_pos = (x - LARGURA_TELA // 2) // TAMANHO_QUADRADO
                    y_pos = -(y - ALTURA_TELA // 2) // TAMANHO_QUADRADO
                    coordenadas_mouse = (x_pos, y_pos)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Obtém as coordenadas do mouse e converte para as coordenadas da malha
                    x, y = event.pos
                    x_pos = (x - LARGURA_TELA // 2) // TAMANHO_QUADRADO
                    y_pos = -(y - ALTURA_TELA // 2) // TAMANHO_QUADRADO
                    coordenadas_mouse = (x_pos, y_pos)

            self.desenhar_malha_tela()

            # Preenche a parte inferior da tela com a cor de fundo das coordenadas
            self.tela.fill(AZUL, (0, ALTURA_TELA - 30, LARGURA_TELA, 30))
            fonte = pygame.font.Font(None, 30)
            texto = fonte.render("Coordenadas do mouse: {}".format(coordenadas_mouse), True, BRANCO)
            pos_texto = texto.get_rect()
            pos_texto.bottomright = (LARGURA_TELA, ALTURA_TELA)
            self.tela.blit(texto, pos_texto)

            pygame.display.flip()


if __name__ == "__main__":
    malha = MalhaQuadriculada()
    malha.executar()