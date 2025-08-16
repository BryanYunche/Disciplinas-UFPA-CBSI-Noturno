"""
Continuação em codificação da lista de funções
"""
"""
Questão 04: Construa a docstring das seguintes funções e renomeie cada função para 
um nome mais apropriado.

a)
def f(*valores):
 M = valores[0]
 for item in valores:
 if item > M:
 M = item
 return M
 
b)
def f(x, y=10, z=5):
 if y > x > z or z > x > y:
 return x
 elif x > y > z or z > y > x:
 return y
 else:
 return z
 
c)
def f(arquivo):
 with open(arquivo, 'r', encoding='utf-8') as f:
 return len(f.readlines())
 
d)
def f(arquivo, arg='teste'):
 with open(arquivo, 'r', encoding='utf-8') as f:
 n = 0
 for item in f:
 if item[:len(arg)] == arg:
 n += 1
 
 return n
 
e)
def f(n=2):
 if n < 2:
 return False
 for q in range(2, n):
 if n % q == 0:
 return False
 
 return True
 
 Exemplo de docstring:
    {Descrição do que faz a função}
    
    Arguments:
        {nome do parâmetro}: {o que é esperado receber} 
    
    Returns:
        {Descrição do que se espera receber}
    
"""


def maiorNumero(*valores):
 """
    Retorna o maior valor em um conjunto de números inteiros.

    :param valores: número(s) inteiros
    :type valores: int

    :return: o maior número da lista
    :rtype: int
 """
 M = valores[0]

 for item in valores:
    if item > M:
    M = item

 return M



def maiorDeTres(x, y=10, z=5):
 """
    Recebe três argumentos do tipo inteiro, e retorna o maior valor
    entre os três.

    :param x: um valor inteiro
    :param y: um valor inteiro (default: 10)
    :param z: um valor inteiro (default: 5)

    :return: retorna qual argumento for maior

 """
 if y > x > z or z > x > y:
    return x
 elif x > y > z or z > y > x:
    return y
 else:
     return z



def contaLinhasArquivo(arquivo):
 """
    Ler um arquivo armazenado em uma variável e ler quantas linhas
    o arquivo tem.

    :param arquivo: arquivo que será aberto ler
    :return: retorna o número de linhas do arquivo
    :rtype: int
 """
 with open(arquivo, 'r', encoding='utf-8') as f:
    return len(f.readlines())


def buscaStringArquivo(arquivo, arg='teste'):
 """
    Verifica se o argumento "arg" está presente no início
    das linhas.

    :param arquivo: espera-se um arquivo de texto
    :param arg: espera-se uma palavra ou sentença
    :type str:
    :return: valor de incidências de arg no inicio de cada linha do documento
    :rtype n: valor inteiro

 """
 with open(arquivo, 'r', encoding='utf-8') as f:
    n = 0
    for item in f:
        if item[:len(arg)] == arg:
            n += 1
    return n


def verificaPrimo(n=2):
 """
    Verifica se é um número primo e retorna true se for primo
    e false se não for primo

    :param n: número inteiro (default: 2)
    :type (int):
    :return: valor booleano
    :rtype: bool
 """
    if n < 2:
        return False
    for q in range(2, n):
        if n % q == 0:
            return False
    return True

