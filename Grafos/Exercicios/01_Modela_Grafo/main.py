from grafo_Matriz_Lista import Grafo

#Exemplo de criação do Grafo por Matriz e Lista de Adjácencias
grafo00 = Grafo()
grafo00.cadastrarGrafos()
grafo00.representacaoGrafo()

#Exemplo Uso do Grafo por Menu
print("----------------- Grafo 01 -----------------")
grafo01 = Grafo()
grafo01.criaGrafo()


#Exemplos de criação do Grafo de forma nomeada
print("----------------- Grafo 02 -----------------")
grafo02 = Grafo(grafosTotais = ['A', 'B', 'C', 'D'], 
                arestasGrafo = [('A', 'B'), ('B', 'A'), ('B', 'C'), ('C', 'B'), ('C', 'A'), ('A', 'C'), ('D', 'B'), ('B', 'D')])
grafo02.apresentaMatrizAdj()

print("----------------- Grafo 03 -----------------")
grafo03 = Grafo(
    grafosTotais = ['X', 'Y', 'Z'],
    arestasGrafo = [('X', 'Y'), ('Y', 'Z'), ('Z', 'X'), ('X', 'Z'), ('Y', 'X')])
grafo03.apresentaMatrizAdj()

print("----------------- Grafo 04 -----------------")
grafo04 = Grafo(
    grafosTotais = ['P', 'Q', 'R', 'S'],
    arestasGrafo = [('P', 'Q'), ('Q', 'R'), ('R', 'S'), ('S', 'P'), ('P', 'R'), ('Q', 'S')])

grafo04.apresentaMatrizAdj()