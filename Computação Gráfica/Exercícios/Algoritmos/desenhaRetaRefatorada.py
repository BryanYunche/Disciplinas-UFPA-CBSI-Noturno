def calculaCoeficienteAngular(x1, y1, x2, y2):
    if x1 == x2:
        return "vertical"
    elif y1 == y2:
        return "horizontal"
    dx = x2 - x1
    dy = y2 - y1
    m = round(dy / dx, 1)
    return m


def transformaOctante(x1, y1, x2, y2):
    m = calculaCoeficienteAngular(x1, y1, x2, y2)

    # Reta vertical
    if m == "vertical":
        x = x1
        y = y1
        return x, y, x1, y1, x2, y2

    # Octante 01 e 05
    if 0 <= int(m) <= 1:
        x = x1
        y = y1
        return x, y, x1, y1, x2, y2

    # Octante 02 e 06
    if int(m) > 1:
        x1, y1, x2, y2 = y1, x1, y2, x2
        x = x1
        y = y1
        return x, y, x1, y1, x2, y2

    # Octante 03 e 07
    if int(m) < -1:
        x1, y1, x2, y2 = y1, -x1, y2, -x2
        x = x1
        y = y1
        return x, y, x1, y1, x2, y2

    # Octante 04 e 08
    if -1 <= int(m) < 0:
        x1, y1, x2, y2 = -x1, y1, -x2, y2
        x = x1
        y = y1
        return x, y, x1, y1, x2, y2

def desfazTransfocacaoOctante(m, lista_pontos):
    pontosDesfeitos = []

    for ponto in lista_pontos:
        x, y = ponto
        # Octante 01 e 05
        if 0 <= int(m) <= 1:
            x, y = x, y
            pontosDesfeitos.append([x, y])

        # Octante 02 e 06
        if int(m) > 1:
            x, y = y, x
            pontosDesfeitos.append([x, y])

        # Octante 03 e 07
        if int(m) < -1:
            x, y = y, -x
            pontosDesfeitos.append([x, y])

        # Octante 04 e 08
        if -1 <= int(m) < 0:
            x, y = -x, y
            pontosDesfeitos.append([x, y])

        # Reta Vertical
        if m == "vertical":
            pontosDesfeitos.append([x, y])

    return pontosDesfeitos


def desenhaRetaVertical(x1, y1, y2):
    # inicio do pontos
    x = x1
    y = y1

    # Pontos da reta
    pontos = [[x, y]]

    if y1 < y2:
        for y in range(y1, y2, 1):
            pontos.append([x, y])
    if y1 > y2:
        for y in range(y1, y2, -1):
            pontos.append([x, y])

    return pontos


def algoritmo_reta(x, y, x1, y1, x2, y2):
    #Desenha reta vertical
    m = calculaCoeficienteAngular(x1, y1, x2, y2)

    if m == "vertical":
        pontos = desenhaRetaVertical(x1, y1, y2)
        return pontos


    # Verifica a ordem de preenchimento da reta
    ordem = '+'
    if x2 < x1:
        ordem = '-'
    if x2 > x1:
        ordem = '+'

    # Inverte a ordem dos pontos caso x2 seja menor que x1
    if x2 < x1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        x, y = x1, y1

    # Pontos da reta
    pontos = [[x, y]]

    # Calcula o coeficiente angular
    m = calculaCoeficienteAngular(x1, y1, x2, y2)

    # Calcula o erro
    e = round(m - (1 / 2), 1)

    while x < x2:

        if e >= 0.0:
            y = y + 1
            e = round(e - 1, 1)
        x = x + 1
        e = round(e + m, 1)

        # Guarda os pontos gerados
        pontos.append([x, y])

    #Inverte a ordem da lista
    if ordem == '-':
        lista = pontos
        lista_invertida = lista[::-1]
        return lista_invertida
    if ordem == '+':
        return pontos

def desenhaReta(x1, y1, x2, y2):
        #Valor referencial do tipo da reta
        m = calculaCoeficienteAngular(x1, y1, x2, y2)

        if m == "vertical":
            # Resolve o problema do OCtante
            x, y, x1, y1, x2, y2 = transformaOctante(x1, y1, x2, y2)
            #Desenha a reta
            pontosTransformados = algoritmo_reta(x, y, x1, y1, x2, y2)
            return pontosTransformados
        else:
            # Resolve o problema do Octante
            x, y, x1, y1, x2, y2 = transformaOctante(x1, y1, x2, y2)
            #Desenha a reta
            pontosTransformados = algoritmo_reta(x, y, x1, y1, x2, y2)
            listaFinalPontos = desfazTransfocacaoOctante(m, pontosTransformados)
            return listaFinalPontos
