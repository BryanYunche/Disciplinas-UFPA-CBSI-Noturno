from AlgortitmosCG.RetaBresenham  import Bresenham

# Função para gerar uma curva de Bezier com base em um número de pontos e pontos de controle
def curvas(nPontos, pontosControle):
    saida = []  # Lista para armazenar os pontos da curva
    pontos = []  # Lista para armazenar os pontos intermediários
    passo = 1 / nPontos  # Passo de avanço ao longo da curva
    t = 0.0  # Parâmetro t inicial

    # Calcula os pontos intermediários ao longo da curva de Bezier
    for d in range(nPontos + 1):
        pontos.append(casteljau(t, pontosControle))
        t += passo

    # Junta os pontos intermediários com retas
    juntar_pontos(pontos, saida)

    return saida  # Retorna a lista de pontos da curva


# Função para calcular um ponto da curva de Bezier usando o algoritmo de Casteljau
def casteljau(t, pontos_controle):
    pts = []
    for p in pontos_controle:
        pts.append(list(p))  # Copia os pontos de controle para uma lista

    # Algoritmo de Casteljau para calcular um ponto da curva de Bezier
    for i in range(1, len(pts)):
        for j in range(len(pts) - i):
            # Atualiza os valores dos pontos intermediários
            pts[j][0] = (1 - t) * pts[j][0] + t * pts[j + 1][0]
            pts[j][1] = (1 - t) * pts[j][1] + t * pts[j + 1][1]

    return [int(pts[0][0]), int(pts[0][1])]  # Retorna o ponto calculado da curva


# Função para juntar os pontos intermediários com retas usando o algoritmo de Bresenham
def juntar_pontos(pontos, saida):
    for x in range(len(pontos) - 1):
        # Cria uma linha reta entre dois pontos usando o algoritmo de Bresenham
        linha = Bresenham(pontos[x][0], pontos[x][1], pontos[x + 1][0], pontos[x + 1][1])

        # Adiciona os pontos da linha à lista de saída
        for pt in linha.saida:
            saida.append(pt)

