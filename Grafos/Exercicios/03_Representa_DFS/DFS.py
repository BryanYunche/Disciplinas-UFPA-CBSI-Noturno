from Grafo import Grafo

#Classe DFS herda da classe Grafo
class DFS(Grafo):
    
    def __init__(self):
        #Chama o construtor de grafo
        super().__init__()
        
        #Adiciona novos atributos
        self.arvores = 0
        self.ciclos = 0
        self.tempo = 0
        self.verticeAnterior = None
        self.dicionarioGrafos = []


    def get_dicionario_grafos(self):
        return self.dicionarioGrafos

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
                self.dicionarioGrafos.append({'Vertice': vertice[0], 
                                              'Adjacencia': [self.get_vertices().index(verticeAdj) for verticeAdj in vertice[1:] if verticeAdj in self.get_vertices()], 
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
            if self.dicionarioGrafos[indiceVerticeAdj]['Cor'] == 'Branco':
                self.verticeAnterior = self.dicionarioGrafos[indiceVisitado].get('Vertice')
                self.DFS_visita_vertice(verticeAnterior, indiceVerticeAdj)
            
            #Identifica ciclos no grafo
            elif self.dicionarioGrafos[indiceVerticeAdj]['Cor'] == 'Cinza':
                self.ciclos += 1

        if self.dicionarioGrafos[indiceVisitado]['Anterior'] != 'Raiz': 
            #Conta um ao finalizar
            self.tempo += 1

            #Pinta de Preto caso saia da pilha
            self.dicionarioGrafos[indiceVisitado]['Cor'] = 'Preto'
            self.dicionarioGrafos[indiceVisitado]['Fim'] = self.tempo
        else:
            #Conta um ao finalizar
            self.tempo += 1
            
            #Pinta de Preto caso saia da pilha
            self.dicionarioGrafos[indiceVisitado]['Cor'] = 'Preto'
            self.dicionarioGrafos[indiceVisitado]['Fim'] = self.tempo
        
            

