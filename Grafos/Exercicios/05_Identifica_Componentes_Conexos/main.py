from DFS import DFS

grafo01 = DFS()

#Adiciona vertices e arestas
grafo01.set_vertices(['A', 'B','C', 'D', 'E','F', 'G', 'H','I'])
grafo01.set_arestas([('A', 'B'), ('B', 'C'), ('C', 'A'),('F', 'G'), ('H', 'F'), ('D', 'H'), ('C', 'D'), ('A', 'C'), ('F', 'I'), ('H', 'I')])

print('=====================================================')
grafo01.DFS_procura()

print('=====================================================')
grafo01.imprime_matriz_adj()

print('=====================================================')
print(f'Quantidade de Ciclos do Grafo: {grafo01.get_ciclos()}')

print('=====================================================')
grafo01.imprime_lista_adj()

print('=====================================================')
for dicio in grafo01.get_dicionario_grafos():
    print(dicio)

