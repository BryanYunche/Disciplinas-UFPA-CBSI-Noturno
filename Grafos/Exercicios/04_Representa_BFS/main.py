from BFS import BFS

#Cria um objeto do tipo DFS que herda todos os métodos de Grafo
grafo01 = BFS()

#Adiciona vertices e arestas
"""grafo01.set_vertices(['A', 'B','C', 'D', 'E','F', 'G', 'H','I'])
grafo01.set_arestas([('A', 'B'), ('F', 'G'), ('H', 'F'), ('D', 'H'), ('C', 'D'), ('A', 'C'), ('F', 'I'), ('H', 'I')])"""

grafo01.set_vertices(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
grafo01.set_arestas([('A', 'B'), ('A', 'C'), ('C', 'D'), ('D', 'H'), ('F', 'G'), ('H', 'F'), ('F', 'I'), ('H', 'I')])


grafo01.BFS_constroi_dicionario()
for dicionario in range(len(grafo01.get_dicionario_grafos())):
    print(grafo01.get_dicionario_grafos()[dicionario])

print('=====================================================')
grafo01.BFS_Busca('A')

for dicionario in range(len(grafo01.get_dicionario_grafos())):
    print(grafo01.get_dicionario_grafos()[dicionario])

print('=====================================================')
grafo01.BFS_Busca('E')

for dicionario in range(len(grafo01.get_dicionario_grafos())):
    print(grafo01.get_dicionario_grafos()[dicionario])

print('=====================================================')
grafo01.encontra_fontes_sumidouro()

print(f'Fontes: {grafo01.get_fontes()}')
print(f'Sumidouros: {grafo01.get_sumidouro()}')

print('=====================================================')
grafo01.imprime_matriz_adj()
