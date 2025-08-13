def produtoCartesiano(verticesA, verticesB, arestasA, arestasB):
    #Realiza o produto entre os Vertices
    verticesW= []
    for x in verticesA:
        for y in verticesB:
            verticesW.append(str(x) + str(y))

    arestasW = []

    #Realiza o produto entre as arestas
    for verticeArestaX, verticeArestaY in arestasA:
        for vertices in verticesB:
            arestasW.append(str(verticeArestaX) + str(vertices))
            arestasW.append(str(verticeArestaY) + str(vertices))

    for verticeArestaX, verticeArestaY in arestasB:
        for vertices in verticesA:
            arestasW.append(str(verticeArestaX) + str(vertices))
            arestasW.append(str(verticeArestaY) + str(vertices))

    #Mostra o resultado do Produto Cartesiano
    print(f'\nVertices do Grafo A: {verticesA}')
    print(f'\nVertices do Grafo B: {verticesB}')
    print("=====================================================================")
    print(f'\nVertices do Grafo A X Grafo B: {verticesW}')

    print(f'\nArestas do Grafo A: {arestasA}')
    print(f'\nArestas do Grafo B: {arestasB}')
    print("=====================================================================")
    print(f'\nArestas do Grafo A X Grafo B: {arestasW}')



    









