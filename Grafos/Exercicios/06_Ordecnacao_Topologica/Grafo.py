class Grafo():

    def __init__(self):
        self.vertices = []
        self.arestas = []
        self.matrizAdj = []
        self.listaAdj = []

    def get_arestas(self):
        return self.arestas
    
    def set_arestas(self, arestas):
        self.arestas = arestas
    
    def adiciona_aresta(self, verticeOrigem, verticeDestino):
        self.arestas.append((verticeOrigem,verticeDestino))

    def get_vertices(self):
        return self.vertices
    
    def set_vertices(self, vertices):
        self.vertices = vertices

    def adiciona_vertices(self, vertice):
        self.vertices.append(vertice)

    def get_matriz_adj(self):
        if self.matrizAdj == []:
            self.gera_matriz_adj()
        return self.matrizAdj
    
    def set_matriz_adj(self, matrizAdj):
        self.matrizAdj = matrizAdj
        self.consome_matriz()
        self.gera_lista_adj()
    
    def get_lista_adj(self):
        return self.listaAdj
    
    def set_lista_adj(self, listaAdj):
        self.listaAdj = listaAdj
    
    #Função Interna
    #Verifica a existências de uma matriz valida
    def validaMatriz(self):
        linhas = len(self.matrizAdj)
        validaMatriz = True
        for i in self.matrizAdj:
            if len(i) != linhas:
                validaMatriz = False
        return validaMatriz

    #Função interna
    def gera_matriz_adj(self):
        #Verifica se o grafo já possui uma matriz de adjacências
        if ((self.matrizAdj == []) and (self.vertices != [])):
            #Cria uma matriz de Adjacências com todos os elementos sendo 0
            self.matrizAdj = [[0 for _ in range(len(self.vertices))] for _ in range(len(self.vertices))]
            xMatriz = 0
            yMatriz = 0
            for verticeX in self.vertices:
                yMatriz = 0
                for verticeY in self.vertices:
                    for aresta in self.arestas:
                        x, y = aresta
                        if (verticeX == x and verticeY == y):
                            self.matrizAdj[xMatriz][yMatriz] = 1
                    yMatriz +=1
                xMatriz +=1

    #Função interna
    #Gera Lista de de ajacências
    def gera_lista_adj(self):
        if ((self.listaAdj == [])):
            listasDeAdjacencias = []
            for vertice in self.vertices:
                listaTemp = []
                listaTemp.append(vertice) 
                for aresta in self.arestas:
                    verticeOrigem, verticeDestino = aresta
                    vertice = str(vertice)
                    verticeOrigem = str(verticeOrigem)
                    if vertice == verticeOrigem:
                        listaTemp.append(verticeDestino)
                listasDeAdjacencias.append(listaTemp)

            self.listaAdj = listasDeAdjacencias

    #Função interna do grafo
    #Cria vertices e arestas a partir da matriz
    def consome_matriz(self):
        if self.validaMatriz():
            self.vertices = [vertice for vertice in range(len(self.matrizAdj))]
            arestas = []
            for linha in range(len(self.matrizAdj)):
                for coluna in range(len(self.matrizAdj)):
                    if self.matrizAdj[linha][coluna] == 1:
                        arestaTemp = (linha,coluna)
                        arestas.append(arestaTemp)
            self.arestas = arestas
    
    #Função interna do grafo
    #Gerar vertices e arestas a partir de uma lista de adjácências no formato:
    #[vertice, adjacência1, adjacência2, adjacência3...]
    def consome_lista(self):
        vertices = []
        arestas = []

        for lista in self.listaAdj:
            if len(lista) == 1:
                vertices.append(lista[0])
            elif len(lista) >= 1:
                vertices.append(lista[0])
                for adj in lista[1:]:
                    tempAresta = (lista[0], adj)
                    arestas.append(tempAresta)
        self.vertices = vertices
        self.arestas = arestas

    #Adicionar funcionalidade para gerar a matriz caso ela não exista ainda
    def imprime_matriz_adj(self):
        #Gera a Matriz de adjacências caso ela não exista ainda.
        self.gera_matriz_adj()

        # Descobrir o comprimento máximo para alinhamento
        max_length = max(len(str(v)) for v in self.vertices + [item for row in self.matrizAdj for item in row])

        # Convertendo os elementos da lista vertices para strings e ajustando o comprimento
        self.vertices = [str(v).ljust(max_length) for v in self.vertices]
        
        # Printar os rótulos das colunas (vértices) com alinhamento
        print(" " * (max_length + 1) + " ".join(self.vertices))
        
        # Printar as linhas com os rótulos à esquerda, ajustando o comprimento
        for i, linha in enumerate(self.matrizAdj):
            row_str = " ".join(str(item).ljust(max_length) for item in linha)
            print(self.vertices[i] + " " + row_str)

    def imprime_lista_adj(self):
        if self.listaAdj == []:
            self.gera_lista_adj()

        for lista in self.listaAdj:
            if len(lista) == 1:
                print(f'Vertice: {lista[0]}\nAdjacêcnias: Não possui.')
                print(10*'_')
            elif len(lista) >= 1:
                vertice = f'Vertice: {lista[0]}'
                adjacencias = ''
                for adj in lista[1:]:
                    adjacencias += f'{adj}, '
                
                print(vertice)
                print(f'Adjacências: {adjacencias[:-2]}')
                print(len(vertice+adjacencias)*'_')