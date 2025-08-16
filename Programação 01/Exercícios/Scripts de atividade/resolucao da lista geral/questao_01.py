"""
João pretende viajar de carro de Paragominas para Belém e gostaria de sua ajuda para
saber o quanto ele irá gastar. Considerando que a distância de Belém para Paragominas
é de 312 km, escreva um algoritmo que dado o preço do litro da gasolina e a autonomia
do carro em km/l calcule o gasto de João.

Preço do litro da
gasolina:
4.1
3.51
3

Autonomia do
carro em km/l:
8.5
10
9.36

Valor esperado
150.49
109.51
100
"""

def calculaGasto(precoGasolina, autonomia, percurso):
    """
    A função calcula o custo de gasolina baseado no percurso
    no gasto de gasolina por litros do carro e o valor da gasolina,
    retornando o valor que foi gasto em gasolina para o percurso

    :param precoGasolina: float
    :param autonomia: float
    :param percurso: float
    :return: float
    """
    litros = percurso/autonomia
    valorGasolina = precoGasolina*litros
    return round(valorGasolina, 2)

print(calculaGasto(4.1, 8.5, 312))



