import matplotlib.pyplot as plt

def desenhar_linha_entre_pontos(pontos):
    # Separar as coordenadas x e y dos pontos
    x = [p[0] for p in pontos]
    y = [p[1] for p in pontos]

    # Criar um gráfico de dispersão com os pontos
    plt.scatter(x, y)

    # Traçar uma linha entre cada par de pontos
    for i in range(len(pontos)-1):
        plt.plot([x[i], x[i+1]], [y[i], y[i+1]])

    # Adicionar linhas de grade
    plt.grid(True)

    # Definir os limites do gráfico com a mesma escala nos eixos x e y
    plt.xlim(min(x)-1, max(x)+1)
    plt.ylim(min(y)-1, max(y)+1)
    plt.axis('equal')

    # Exibir o gráfico
    plt.show()