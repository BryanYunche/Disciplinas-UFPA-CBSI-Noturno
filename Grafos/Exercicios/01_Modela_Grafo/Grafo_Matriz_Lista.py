class Grafo:
    def __init__(self, listaAdjacencias = [], matrizAdjacencias = [], grafosTotais = [], arestasGrafo = []):
        self.matrizAdjacencias = matrizAdjacencias
        self.listaAdjacencias = listaAdjacencias
        self.grafosTotais = grafosTotais
        self.arestasGrafo = arestasGrafo

    #-------------------------------------------------------------------------------------
    def criaGrafo(self):
        vertices = input("Digite Quantos Vertices possuirá o Grafo: ")
        vertices = int(vertices.strip())


        print("----------------------------------------------------")
        print("            Menu de Criação de Grafo                ")
        print("----------------------------------------------------")
        print("Digite [1] para adicionar vertices ao Grafo         ")
        print("Digite [2] para Adicionar arestas entre os Vertices ")
        print("Digite [3] para visualizar os vertices do Grafo     ")
        print("Digite [4] para visualizar a a lista de Adjacencias ")
        print("Digite [5] para visualizar a Matriz de Adjacencias  ")
        print("Digite [6] para visualizar o Grafo todo             ")
        print("Digite [0] para Sair                                ")
        print("----------------------------------------------------")
        escolha = input("Digite sua escolha: ")
        escolha = int(escolha.strip())

        if escolha == 1:
            self.adicionaVertices()
        elif escolha == 2:
            self.adicionaAresta()
        elif escolha == 3:
            self.apresentaListaAdj()
        elif escolha == 4:
            self.apresentaMatrizAdj()
        elif escolha == 5:
            self.representacaoGrafo()
        elif escolha == 6:
            self.apresentaMatrizAdj()
        elif escolha == 0:
            print("Encerra Programa!")
        else:
            self.criaGrafo()

    #-------------------------------------------------------------------------------------
    def adicionaAresta(self):
        while True:
            try:

                verticeSaida = ''
                print("-------------------------------------------------------")
                print(f'Arestas: {self.arestasGrafo}')
                print("-------------------------------------------------------")
                print(f'Vertices: {self.grafosTotais}')
                verticeSaida = input('Digite o Vertice de saida da aresta: ')
                verticeSaida = int(verticeSaida.strip())

                if verticeSaida not in self.grafosTotais:
                    print("Vertice não encontrado!")
                else:
                    while True:
                        verticeEntrada = ''
                        try:
                            print("-------------------------------------------------------")
                            print(f'Vertices: {self.grafosTotais}')
                            verticeEntrada = input('Digite o Vertice de entrada da aresta: ')
                            verticeEntrada = verticeEntrada.strip()

                            if verticeEntrada not in self.grafosTotais:
                                print("Vertice não encontrado!")
                            else:
                                # Adiciona a aresta efetivamente
                                self.arestasGrafo.append((verticeSaida, verticeEntrada))
                                print(f'Aresta {verticeSaida} --> {verticeEntrada} cadastrada com sucesso!')
                                
                                # Sai do loop interno após a adição da aresta
                                break  

                        except ValueError:
                            print("Digite um vertice válido!")

            except ValueError:
                print("Digite um vertice válido!")

            # Sai do loop 
            break
               
        #Volta ao Menu
        self.criaGrafo()

    #-------------------------------------------------------------------------------------       
    def criaListaAdj(self):
        self.listaAdjacencias = []  

        for vertice in self.grafosTotais:
            listaAdjTemp = [vertice]  

            for aresta in self.arestasGrafo:
                if aresta[0] == vertice:
                    listaAdjTemp.append(aresta[1])

            # Adiciona a lista de adjacências para o vértice atual
            self.listaAdjacencias.append(listaAdjTemp)

        return self.listaAdjacencias

    def apresentaListaAdj(self):
        listaAdj = self.criaListaAdj()  

        for lista in listaAdj:
            vertice = lista[0]  
            adjacente = lista[1:]  

            subListaAdj = f'{vertice}:'

            # Verifica se há adjacentes e os adiciona à string
            if adjacente:
                for adj in adjacente:
                    subListaAdj += f' ---> {adj}'
            else:
                subListaAdj += ' Nenhum adjacente'

            # Imprime a lista de adjacências do vértice atual
            print(f'Adjacências do vértice {vertice}: [ {subListaAdj.strip()} ]')

    #-------------------------------------------------------------------------------------
    def criaMatrizAdj(self):
        matrizAdj = []
        
        for verticeX  in self.grafosTotais:
            linhaTemp = []
            for verticeY in self.grafosTotais:
                if ((verticeX, verticeY) in self.arestasGrafo):
                    linhaTemp.append('1')
                else:
                    linhaTemp.append('0')

            #Adiciona efetivamente uma linha matriz
            matrizAdj.append(linhaTemp)
        
        #Adiciona a Matriz de Adjacências como atributo no grafo
        self.matrizAdjacencias = matrizAdj

        return self.matrizAdjacencias
    
    def apresentaMatrizAdj(self):

        #Gera MAtriz de adjacências  
        self.criaMatrizAdj()

        #Contador para iterar a inserção do vertice correspondente de cada linha
        cont = 0

        #Espaço da coluna dos outros vertices
        print("   ", end='|')

        #Linha de cima da Matriz
        for vertices in self.grafosTotais:
            print(f' {vertices} ', end='|')

        #Tamanho do tracejado ajustado de acordo com o tamanho da Matriz
        print('\n' + len(self.grafosTotais)*6*"=")

        #Valor Real da Matriz
        for linha in self.matrizAdjacencias:
            linha.insert(0, self.grafosTotais[cont])
            for valor in linha:
                print(f' {valor} ', end='|')
            print()
            print((len(self.matrizAdjacencias)*6*"="))

            cont += 1

    #-------------------------------------------------------------------------------------
    def adicionaVertices(self):
        listaVertices = []
        while True:
            try:
                vertices = input("Inserir um numero de vertices: ")
                vertices = int(vertices.strip())
                print(f'Você inseriu {vertices}')

                #Gera uma lista de vertices
                if vertices >= 1:
                    for i in range(1, vertices + 1):
                        listaVertices.append(i)
                else:
                    print("Seu valor não é válido como número de arestas!")
                self.grafosTotais = listaVertices

                break
            except ValueError:
                print("Erro: Por favor, insira um número inteiro válido.")
            
        #Volta ao Menu
        self.criaGrafo()

    #------------------------------------------------------------------------------------- 
    def representacaoGrafo(self):
        print(f'Vertices: {self.grafosTotais}')
        print(f'Arestas: {self.arestasGrafo}')

        while True:
            escolha = input("Deseja Retornar ao Menu? [y/n]: ")
            escolha = escolha.strip()

            if escolha == 'y':
                self.criaGrafo()
            elif escolha == 'n':
                print("Programa Encerrado!")
            else:
                print("Entrada Inválida!")
                self.representacaoGrafo()

    #-------------------------------------------------------------------------------------
    def cadastrarGrafos(self):
        tipoGrafo = '0'
        escolha = input('Deseja cadastrar um Grafo [y/n]: ')
        escolha = escolha.strip().lower()

        #Decide a forma de cadastro do Grafo
        if escolha == 'y':
            print("Que forma você deseja cadastrar seus Grafos?")
            print("Digite [1] para lista de adjacências.")
            print("Digite [2] para Matriz de adjacências.")
            print("Digite [0] para Sair.")

            tipoGrafo = input("Digite sua Escolha: ")
            tipoGrafo = tipoGrafo.strip().lower()
            
        elif escolha == 'n':
            print("Cadastro Encerrado!")
        else:
            print("Digite um valor Válido!")
            self.cadastrarGrafos()
        
        #Cadastra efetivamente o Grafo
        if tipoGrafo == '1':
            self.cadastraListaAdjacencias()
        elif tipoGrafo == '2':
            self.cadastraMatrizAjacencias()
        elif tipoGrafo == '0':
            pass
        else:
            print("Houve um erro ao decidir o tipo de cadastro!")
            self.cadastrarGrafos()
    
    #-------------------------------------------------------------------------------------
    def cadastraListaAdjacencias(self):
        #Inicio Variaveis
        grafo = ''
        cadLista = 'y'
        listaArestas = []
        listaGrafosTotais = []

        while cadLista == 'y':

            #Inicio Variáveis
            adjacencia = ''
            grafo = ''
            listaAdjacenciasTemp = []


            #Cadastra o Grafo principal que terá suas Adjacencias digitadas
            print("Cadastro de Nova Lista de Adjacencias!!")
            grafo = input(f'Digite o nome do Grafo que será inserido as Adjacências: ')
            grafo = str(grafo.strip()).lower()
            listaAdjacenciasTemp.append(grafo)


            #Cadastra Adjacências do Grafo
            while True:
                #Insere grafo
                print("Digite 'sair' caso queira encerra o ESTA lista Adjacências!!!")
                adjacencia = input(f'Insira um Grafo Adjacente de {grafo}: ')

                #Valida se o usuário quer sair
                if adjacencia == "sair":
                    break
        
                #Trata e insere a adjasencia
                adjacencia = adjacencia.strip().lower()
                listaAdjacenciasTemp.append(adjacencia)

                #Valida mais adjacencias
                print("------------------------------------------------------------------")
                print(f'Lista de Adjacências do Grafor {grafo} atualizada!')
                print(f'Lista atual de Adjacências: {listaAdjacenciasTemp}')
                print("------------------------------------------------------------------")

                #Registra Aresta
                listaArestas.append((grafo, adjacencia))
            
            #Valida se o usuário quer inserir mais uma lista de adjacencias
            if cadLista == 'y':
                while True:
                    cadLista = input('Deseja cadastrar outra lista de Adjacencias? [y/n]: ')
                    cadLista = cadLista.strip().lower()
                    if cadLista not in ['y', 'n']:
                        print('Coloque uma entrada válida!')
                    else:
                        print("Cadastro Encerrado!")
                        break


            #Insere na Lista de feita a lista maior
            self.listaAdjacencias.append(listaAdjacenciasTemp)

        #Calcula os vertices encontrados na lista de Ajacências
        for linha in self.listaAdjacencias:
            for grafinho in linha:
                listaGrafosTotais.append(grafinho)
        
        #Remove as duplicatas 
        self.grafosTotais = list(set(listaGrafosTotais))

        
        #Atualiza o Valor de arestas do Grafo
        self.arestasGrafo.extend(listaArestas)

    #-------------------------------------------------------------------------------------
    def cadastraMatrizAjacencias(self):
        grafo = ''
        aresta = ''
        listaAresta = []

        #Cadastra os Grafos da Matriz
        print("--[Digite 'concluir' para sair do cadastro de grafos da Matriz de Adjacencias]---")
        print("--[Insira os grafos que serão detalhados na MAtriz de Adjacências]--")
        while grafo != 'concluir':
            grafo = input(f'Digite o nome do Grafo: ')
            grafo = str(grafo.strip()).lower()
            self.grafosTotais.append(grafo)
        
        #Retira a palavra concluir da lista de grafos
        self.grafosTotais.pop()
        
        #Mostra ao Usuário a lista de Grafos
        print("------------------------------------------------")
        print(f'Grafos registrados: {self.grafosTotais}')
        print("------------------------------------------------")

        #Produz a Matriz de Adjacências
        for grafoColuna in self.grafosTotais:
            linhaTemp = []
            for grafoLinha in self.grafosTotais:
                    print('Digite [1] para Verdadeiro e [0] para Falso')
                    aresta = input(f'Aresta: {grafoColuna} --> {grafoLinha}: ')
                    aresta = aresta.strip().lower()
                    linhaTemp.append(aresta)

                    #Registra Aresta
                    if aresta != '0':
                        listaAresta.append((grafoColuna, grafoLinha))   

            #Atualiza a Matriz do grafo geral
            self.matrizAdjacencias.append(linhaTemp)
        
        #Atualiza o Valor de arestas do Grafo
        self.arestasGrafo.extend(listaAresta) 
    
    #-------------------------------------------------------------------------------------
    def getVertices(self):
        return self.grafosTotais

    #-------------------------------------------------------------------------------------
    def getArestas(self):
        return self.arestasGrafo
    
        