from grafo_Matriz_Lista import Grafo
from produtoVetorialGrafo import produtoCartesiano

print("----------------- Grafo 02 -----------------")
grafo01 = Grafo(grafosTotais = ['A', 'B', 'C', 'D'], 
                arestasGrafo = [('A', 'B'), ('B', 'A'), ('B', 'C'), ('C', 'B'), ('C', 'A'), ('A', 'C'), ('D', 'B'), ('B', 'D')])
grafo01.apresentaMatrizAdj()
grafo01.apresentaListaAdj()

print("=====================================================================")

print("----------------- Grafo 03 -----------------")
grafo02 = Grafo(
    grafosTotais = ['X', 'Y', 'Z'],
    arestasGrafo = [('X', 'Y'), ('Y', 'Z'), ('Z', 'X'), ('X', 'Z'), ('Y', 'X')])
grafo02.apresentaMatrizAdj()
grafo02.apresentaListaAdj()

print("=====================================================================")

print("----------------- Grafo 04 -----------------")
grafo03 = Grafo(
    grafosTotais = ['P', 'Q', 'R', 'S'],
    arestasGrafo = [('P', 'Q'), ('Q', 'R'), ('R', 'S'), ('S', 'P'), ('P', 'R'), ('Q', 'S')])

grafo03.apresentaMatrizAdj()
grafo03.apresentaListaAdj()

print("=====================================================================")

produtoCartesiano(grafo01.grafosTotais, grafo02.grafosTotais, grafo01.arestasGrafo, grafo02.arestasGrafo)
produtoCartesiano()

