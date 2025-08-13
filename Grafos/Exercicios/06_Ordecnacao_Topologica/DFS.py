from Grafo import Grafo

#Classe DFS herda da classe Grafo
class DFS(Grafo):
    
    def __init__(self):
        #Chama o construtor de grafo
        super().__init__()
        
        #Adiciona novos atributos
        self.arvores = 0
        self.ciclos = False
        self.tempo = 0
        self.verticeAnterior = None
        self.dicionarioGrafos = []
        self.ordem_topologica = []


    def get_dicionario_grafos(self):
        return self.dicionarioGrafos
    
    def get_ciclos(self):
        return self.ciclos
    
    def get_ordem_topologica(self):
        return self.ordem_topologica

    #Constroi dicionário de grafos Brancos
    def DFS_constroi_dicionario(self):
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

                #faz uma lista dos indices vertices adjacentes
                verticesAdjTemp = []
                for verticeAdj in vertice[1:]:
                    verticeAdj = str(verticeAdj)
                    verticesAdjTemp.append(self.vertices.index(verticeAdj))            
                
                self.dicionarioGrafos.append({'Vertice': vertice[0], 
                                              'Adjacencia': verticesAdjTemp, 
                                              'Cor': 'Branco', 
                                              'Anterior': None,
                                              'Inicio': 0, 
                                              'Fim': 0})  
            elif len(vertice) == 1:
                self.dicionarioGrafos.append({'Vertice':vertice[0], 
                                              'Adjacencia': None, 
                                              'Cor': 'Branco', 
                                              'Anterior': None,
                                              'Inicio': 0, 
                                              'Fim': 0})
            
    def DFS_procura(self):
        if self.dicionarioGrafos == []:
            self.DFS_constroi_dicionario()
        
        for i in range(len(self.dicionarioGrafos)):
            if self.dicionarioGrafos[i].get('Cor') == 'Branco':
                self.dicionarioGrafos[i]['Anterior'] = 'Raiz'
                self.DFS_visita_vertice(self.dicionarioGrafos[i].get('Vertice'), i)
                
                #A cada vez que o algoritimo volta a esse laço, quer dizer que ele saiu de uma arvore
                #Logo, pode ser identificado uma arvore
                self.arvores += 1 

                #Quando inicia uma arvore nova adiciona mais um no contador do tempo
                
                #Conta um ao tempo do contador
                self.tempo += 1
        
        self.ordem_topologica = self.ordem_topologica[::-1]

    #Percorre Grafo (Terminar de fazer isso)
    def DFS_visita_vertice(self, verticeAnterior, indiceVisitado):
        self.dicionarioGrafos[indiceVisitado]['Cor'] = 'Cinza'
        self.dicionarioGrafos[indiceVisitado]['Inicio'] = self.tempo

        #Verifica se o vertice não é uma Raiz
        if self.dicionarioGrafos[indiceVisitado]['Anterior'] != 'Raiz':
           self.dicionarioGrafos[indiceVisitado]['Anterior'] = self.verticeAnterior

        #Conta um ao tempo do contador
        self.tempo += 1
        for indiceVerticeAdj in self.dicionarioGrafos[indiceVisitado].get('Adjacencia'):
            #Identifica ciclos no grafo
            if self.dicionarioGrafos[indiceVerticeAdj]['Cor'] == 'Cinza':
                self.ciclos = True
                
            #Vai para o próximo grafo
            elif self.dicionarioGrafos[indiceVerticeAdj]['Cor'] == 'Branco':
                self.verticeAnterior = self.dicionarioGrafos[indiceVisitado].get('Vertice')
                self.DFS_visita_vertice(verticeAnterior, indiceVerticeAdj)

        if self.dicionarioGrafos[indiceVisitado]['Anterior'] != 'Raiz': 
            #Conta um ao finalizar
            self.tempo += 1

            #Pinta de Preto caso saia da pilha
            self.dicionarioGrafos[indiceVisitado]['Cor'] = 'Preto'
            self.dicionarioGrafos[indiceVisitado]['Fim'] = self.tempo
            self.ordem_topologica.append(self.dicionarioGrafos[indiceVisitado]['Vertice'])
        else:
            #Conta um ao finalizar
            self.tempo += 1

            #Pinta de Preto caso saia da pilha
            self.dicionarioGrafos[indiceVisitado]['Cor'] = 'Preto'
            self.dicionarioGrafos[indiceVisitado]['Fim'] = self.tempo
            self.ordem_topologica.append(self.dicionarioGrafos[indiceVisitado]['Vertice'])
        
            
    def detalhes_Grafo(self):
        self.imprime_matriz_adj()
        print("===============================================")
        self.DFS_procura()
        for dicionario in range(len(self.get_dicionario_grafos())):
            print(self.get_dicionario_grafos()[dicionario])

        print("===============================================")
        print(f'O grafo possui Ciclos: {self.get_ciclos()}')
        print("===============================================")
        #valida se é um DAG, se possuir ciclos não é um dag!
        print(f'O grafo é um DAG?: {False if self.get_ciclos() else True}')
        print("===============================================")
        print(f'Ordem topológica do Grafo: {self.get_ordem_topologica()}')
        print("===============================================")
        self.imprime_lista_adj()
