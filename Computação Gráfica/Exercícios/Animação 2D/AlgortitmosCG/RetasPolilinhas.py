from AlgortitmosCG.RetaBresenham import Bresenham

def polilinha(*pontos, fechaPoligono=False):

    #Varre os pontos e os transforma em listas menores de pontos
    listaTemp = []
    for indice in range(0, len(pontos)-1, 2):
        x = pontos[indice]
        y = pontos[indice+1]
        listaTemp.append([x, y])

    #print(listaTemp)
    # ----------------------------------------------------------

    #Define as retas a ser desenhadas a partir dos pontos
    retas = []
    if len(listaTemp) >= 2:
        for i in range(0, len(listaTemp) - 1):
            inicioReta = listaTemp[i]
            finalReta = listaTemp[i + 1]
            retas.append([inicioReta, finalReta])

    #Liga o final do poligono ao inicio
    if fechaPoligono:
        retas.append([listaTemp[-1], *listaTemp[0:1]])

    #print(retas)
    # ----------------------------------------------------------

    #Transforma os pontos em uma lista organizada
    pontosDasRetas = []
    for indice in range(0, len(retas)):
        retaTemporaria = retas[indice]
        for i in range(0, len(retaTemporaria)):
            x, y = retas[indice][i]
            pontosDasRetas.append(x)
            pontosDasRetas.append(y)

    #print(pontosDasRetas)
    # ----------------------------------------------------------

    #pega os argumentos apenas para uma reta
    argumetosParaRetas = []

    #Aqui a iteração começa no inicio pois a primeira iteração é desconsiderada
    for argumentos in range(1, len(pontosDasRetas)+1):
        #Faz os fatiamentos de 4 em 4 que é o valor dos argumentos necessários para fazer uma reta
        #Para fazer o fatiamento de 4 em 4 utilizamos os multiplos de 4
        if argumentos%4 == 0:
            argumetosParaRetas.append(pontosDasRetas[argumentos-4:argumentos])

    #print(argumetosParaRetas)
    # ----------------------------------------------------------

    #Vai armazenar os pontos gerados pelo bresenhan
    pontosDoBresenham = []
    #Começa a aplicar bresenham para pegar os pontos
    for argumento in argumetosParaRetas:
        x1, y1, x2, y2 = argumento
        bresenham = Bresenham(x1, y1, x2, y2)
        pontosTemporarios = bresenham.saida

        #print(pontosTemporarios)

        #Adiciona as retas de bresenham em um só vetor
        pontosDoBresenham.append(pontosTemporarios)

        #print(pontosDoBresenham)
    # ----------------------------------------------------------

    #Desencapsula as retas para ficar legível para a função de plot
    pontosDesencapsulados = []
    for args in pontosDoBresenham:
        for z in args:
            pontosDesencapsulados.append(z)

    #print(pontosDesencapsulados)

    return pontosDesencapsulados

#print(polilinha(3, 2, 3, 6, 7, 6, 7, 2))
