import desenhaRetaCG as rt

def verificaPontos(arestas, pontos):
    verifica01 = False
    verifica02 = False
    verifica03 = False

    #Verifica se são todos números inteiros:
    cont=0
    for valor in pontos:
        if type(valor) == int:
            cont+=1
    if cont == len(pontos):
        verifica01 = True

    #Verifica se o número de arestas é o mesmo dos pontos passados
    if (arestas == len(pontos)/2):
        verifica02 = True

    #Verifica os pontos formam um plogono mínimo
    if(arestas >= 3):
        verifica03 = True

    return verifica01 and verifica02 and verifica03


def poligonoQualquer(arestas, *lista_pontos):
    pontos = lista_pontos
    #Valida os argumentos da função
    validador = verificaPontos(arestas, pontos)

    #----------------------------------------------------------
    #Varre os pontos
    listaTemp = []
    for indice in range(0, len(pontos)-1, 2):
        x = pontos[indice]
        y = pontos[indice+1]
        listaTemp.append([x, y])

    # ----------------------------------------------------------
    #Define as retas
    retas = []
    numero = [0, 1, 2, 3]
    for indice in range(0, len(listaTemp)-1, 1):
        retas.append([listaTemp[indice], listaTemp[indice+1]])

    #Liga o final do poligono ao inicio
    retas.append([listaTemp[-1], *listaTemp[0:1]])

    # ----------------------------------------------------------
    #Organiaza as retas em um único vetor de informações
    pontosDasRetas = []
    for indice in range(0, len(retas)):
        retaTemporaria = retas[indice]
        for i in range(0, len(retaTemporaria)):
            x, y = retas[indice][i]
            pontosDasRetas.append(x)
            pontosDasRetas.append(y)

    # ----------------------------------------------------------
    #pega os argumentos apenas para uma reta
    argumetosParaRetas = []
    for argumentos in range(1, len(pontosDasRetas)+1):
        #Faz os fatiamentos de 4 em 4 que é o valor dos argumentos necessários para fazer uma reta
        if argumentos%4 == 0:
            argumetosParaRetas.append(pontosDasRetas[argumentos-4:argumentos])

    # ----------------------------------------------------------
    #Desenha retas
    pontosDesenhados = []
    for args in argumetosParaRetas:
        x1, y1, x2, y2 = args
        pontosDesenhados.append(rt.bresenham_line(x1, y1, x2, y2))

    # ----------------------------------------------------------
    #Apenas desencapsula os pontos das retas
    pontosDesencapsulados = []
    for args in pontosDesenhados:
        for z in args:
            pontosDesencapsulados.append(z)

    return pontosDesencapsulados

#print(poligonoQualquer(4, 3, 2, 3, 6, 7, 6, 7, 2))