from DFS import DFS

#List de Grafos
#Grafo 01
grafo01 = DFS()
matriz = [[0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0]]

grafo01.set_matriz_adj(matriz)

# Grafo 02
grafo02 = DFS()
matriz = [[0, 1, 0, 0, 1],
          [1, 0, 1, 1, 0],
          [0, 1, 0, 0, 1],
          [0, 1, 0, 0, 1],
          [1, 0, 1, 1, 0]]

grafo02.set_matriz_adj(matriz)

# Grafo 03 (DAG)
grafo03 = DFS()
matriz = [[0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 0, 1, 1],
          [0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0]]

grafo03.set_matriz_adj(matriz)

# Grafo 04
grafo04 = DFS()
matriz = [[0, 1, 1, 0, 0, 0],
          [1, 0, 1, 1, 0, 0],
          [1, 1, 0, 1, 1, 0],
          [0, 1, 1, 0, 1, 0],
          [0, 0, 1, 1, 0, 1],
          [0, 0, 0, 0, 1, 0]]

grafo04.set_matriz_adj(matriz)

#Grafo 02

print("===============================================")
grafo01.detalhes_Grafo()
print("===============================================")
grafo02.detalhes_Grafo()
print("===============================================")
grafo03.detalhes_Grafo()
print("===============================================")
grafo04.detalhes_Grafo()