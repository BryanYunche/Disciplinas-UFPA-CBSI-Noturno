from Grafo import Grafo

class BFS(Grafo):

    def __init__(self):

        #Chama o construtor do Grafo
        super().__init__()
        
        #Atributos BFS
        self.fila_vertices = []
        self.fila_de_vertices_visitados = []
        self.vertice_anterior = []
        self.distancia = 0
        self.arvore = []

        #Informações extraidas do grafo
        self.dicionarioGrafos = []

        #Determina fonte e sumidouro do grafo
        self.vertices_Fonte = []
        self.vertices_Sumidouro = []
        self.vertices_isolados = []
        self.matriz_Adj_transposta = []

    def get_dicionario_grafos(self):
        return self.dicionarioGrafos
    
    def get_fontes(self):
        return self.vertices_Fonte
    
    def get_sumidouro(self):
        return self.vertices_Sumidouro

    def BFS_constroi_dicionario(self):
        #Gera a lista de aDjacências caso não exista ainda 
        self.gera_lista_adj()

        #Constroi os dicionários
        for vertice in self.get_lista_adj():
            #O if não altera a ordem dos vertices
            #As adjácencias guardam o indice de onde está o vertice no dicionário
            if len(vertice) >= 1:
                #Considerando que a ordem das listas de adjacencias é igual a ordem da lista de vertices
                #Usarei a lista de vertices para identificar o indice dos dicionários
                #Substituirei as adjacencias pelo indice dos vertices que seriam essas adjacências
                self.dicionarioGrafos.append({'Vertice': vertice[0], 
                                              'Adjacencia': [self.get_vertices().index(verticeAdj) for verticeAdj in vertice[1:] if verticeAdj in self.get_vertices()], 
                                              'Visitado': False, 
                                              'Anterior': None,
                                              'Distancia': 0,
                                              'Vertice Fonte': None,
                                              'Arvore': []})  
            elif len(vertice) == 1:
                self.dicionarioGrafos.append({'Vertice':vertice[0], 
                                              'Adjacencia': None, 
                                              'Visitado': False, 
                                              'Anterior': None,
                                              'Distancia': 0,
                                              'Vertice Fonte': None,
                                              'Arvore': []})
                
    def encontra_fontes_sumidouro(self):
            indiceMatraiz = len(self.get_matriz_adj())
            
            #Defini matriz transposta
            matriz_Adj_transposta = [[self.get_matriz_adj()[j][i] for j in range(len(self.get_matriz_adj()))] for i in range(len(self.get_matriz_adj()[0]))]

            #Preenche a matriz transposta // Usada Para identificar fontes caso a some de sua linha seja igual a zero
            for linha in range(indiceMatraiz):
                for coluna in range(indiceMatraiz):
                    matriz_Adj_transposta[coluna][linha] = self.get_matriz_adj()[linha][coluna]
            
            for vertice in range(indiceMatraiz):
                if (sum(self.get_matriz_adj()[vertice]) == 0) and (sum(matriz_Adj_transposta[vertice]) == 0):
                    self.vertices_isolados.append(self.dicionarioGrafos[vertice]['Vertice'])
                elif (sum(matriz_Adj_transposta[vertice]) == 0):
                    self.vertices_Fonte.append(self.dicionarioGrafos[vertice]['Vertice'])
                elif (sum(self.get_matriz_adj()[vertice]) == 0):
                    self.vertices_Sumidouro.append(self.dicionarioGrafos[vertice]['Vertice'])
                
    def BFS_Busca(self, vertice):

        #Reinicia arvore
        self.arvore = []


        if self.dicionarioGrafos[self.get_vertices().index(vertice)]['Visitado'] == False:

            #Preenche o vertice raiz
            self.dicionarioGrafos[self.get_vertices().index(vertice)]['Visitado'] = True
            self.dicionarioGrafos[self.get_vertices().index(vertice)]['Anterior'] = 'Raiz'
            self.dicionarioGrafos[self.get_vertices().index(vertice)]['Distancia'] = self.distancia
            self.dicionarioGrafos[self.get_vertices().index(vertice)]['Vertice Fonte'] = vertice

            #Define vertice fonte
            vertice_fonte = vertice

            #Garante que vai buscar pelo menos uma adjacência
            if self.dicionarioGrafos[self.get_vertices().index(vertice)]['Adjacencia'] != []:

                #A fila recebe o indice do vertice fonte que irá ser buscados
                self.fila_vertices.append(self.get_vertices().index(vertice))
                
                while(self.fila_vertices != []):

                    #verifica se o próximo vertice a ser processado tem adjacências
                    if self.dicionarioGrafos[self.fila_vertices[0]]['Adjacencia'] != []:

                        #Para cada lista de adjacencias que entra na fila de vertices será registrado o vertice ANTERIOR e a DISTANCIA 
                        for adj in self.dicionarioGrafos[self.fila_vertices[0]]['Adjacencia']:
                            self.dicionarioGrafos[adj]['Anterior'] = vertice
                            self.dicionarioGrafos[adj]['Distancia'] = self.distancia
                            self.dicionarioGrafos[self.fila_vertices[0]]['Vertice Fonte'] = vertice_fonte
                            #Adjacencias entram para a fila
                            self.fila_vertices.append(adj)
                        
                        #Incrementa distância
                        self.distancia += 1
                            
                        #Vertice que será processado / Retira da lista e é usado como indice para preencher os dados do dicionário
                        indice_vertice_processado = self.fila_vertices.pop(0)

                        #Constroi arvore
                        self.arvore.append(indice_vertice_processado)

                        self.dicionarioGrafos[indice_vertice_processado]['Visitado'] = True

                        #Muda o valor de vertice para o próximo da fila a ser iterado
                        vertice = self.fila_vertices[0]

                    #Se o vertice não tiver adjacencias
                    elif self.dicionarioGrafos[self.fila_vertices[0]]['Adjacencia'] == []:
                        self.dicionarioGrafos[vertice]['Anterior'] = self.fila_vertices[0]
                        self.dicionarioGrafos[vertice]['Distancia'] = self.distancia + 1
                        self.dicionarioGrafos[self.fila_vertices[0]]['Visitado'] = True
                        self.dicionarioGrafos[self.fila_vertices[0]]['Vertice Fonte'] = vertice_fonte
                        
                        #Retira o indice e constroi arvore
                        self.arvore.append(self.fila_vertices.pop(0))
                
                #Preenche arvore
                self.controi_arvore(vertice_fonte)

            #Se o vertice fonte não possuir uma adjacência a arvore dele será ele mesmo
            elif (self.dicionarioGrafos[self.get_vertices().index(vertice_fonte)]['Adjacencia'] == []) and (self.dicionarioGrafos[self.get_vertices().index(vertice_fonte)]['Vertice Fonte'] == vertice_fonte):
                self.dicionarioGrafos[self.get_vertices().index(vertice_fonte)]['Arvore'] = [vertice_fonte] 

    
    def controi_arvore(self, vertice_raiz):
        for dicionario in self.dicionarioGrafos:
            if vertice_raiz == dicionario['Vertice Fonte']:
                dicionario['Arvore'] = [self.vertices[indice_vertice] for indice_vertice in self.arvore]
                 

                            
                    
                        


                
        