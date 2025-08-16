'''
Questão 01: Escreva uma função chamada merge. 
Essa função deve ter dois parâmetros: 
o primeiro deve ser chamado de saudação e o segundo deve ser chamado de nome. 
A função deve concatenar os valores tendo um espaço no meio. 
Caso nenhum parâmetro seja passado para saudação, ele deverá ter como valor padrão “olá”. 
Retorne a string concatenada.

Questão 02: 
a) Chame a função merge passando dois argumentos de forma posicional. 
b) Chame a função merge passando um argumento. 
c) Chame a função merge passando dois argumentos de forma nomeada.

Questão 03: 
Escreva uma função chamada lista_homogenea. 
Essa função deve ter dois parâmetros chamados de valor e N. 
A função deve retornar uma lista de tamanho N onde todos os valores são iguais ao valor armazenado no parâmetro valor. 
Por padrão, a função deve gerar uma lista de tamanho 10 contendo elementos zeros. 
Retorne a lista gerada.

Questão 04: 
Escreva uma função chamada primeiro_eh_maior. 
Essa função deve receber 2 argumentos e retornar True caso o primeiro argumento seja o maior. 
Caso contrário, deve retornar False. 
A função não deve ter parâmetros com valor default.

Questão 05: 
Escreva uma função chamada maxMin. 
Essa função deve receber um número indeterminado de argumentos. 
A função deve retornar o maior e o menor valor passado como argumento. 
No escopo da sua função, utilize a função max e min para encontrar os valores. 
No retorno da função, realize um retorno múltiplo para retornar os dois valores.

Questão 06: 
Escreva uma função chamada somar. 
Essa função deve receber um número indeterminado de argumentos. 
A função deve retornar a soma dos elementos, excluindo o maior e o menor valor. 
Considere que todos os argumentos passados possuem valores distintos.

Questão 07
Escreva uma função para receber 4 argumentos.
Essa função deve retornar true caso os argumentos estejam ordenados alfabeticamente.
Caso contrário deve retornar false.
Considere que os argumentos são do tipo string
'''

#Questão 01
def merge(saudacao = 'Olá', nome = "Pessoa"):
    str_concatenada = saudacao+ ' ' + nome
    return str_concatenada

#Questão 02
merge("Boa noite", "Bryan")
merge(nome="Bryan")
merge(nome="Bryan", saudacao="Bom dia")

#Questão 03
def lista_homogenea(valor=0, N=10):
    lista = N*[valor]
    return lista

#Questão 04
def primeiro_eh_maior(valor1, valor2):
   return x>y

#Questão 05
def maxMin(*n):
    maximo = max(n)
    minimo = min(n)
    return maximo, minimo

#Questão 06
def somar(*n):
    valores_somados = 0
    lista = n
    menor = min(lista)
    maior = max(lista)

    for soma in lista:
        valores_somados += soma
    
    valores_somados -= (menor+maior)

    return valores_somados

#Questão 07
def ordenada(a, b, c, d):
    return(a<b<c<d)


        


    








