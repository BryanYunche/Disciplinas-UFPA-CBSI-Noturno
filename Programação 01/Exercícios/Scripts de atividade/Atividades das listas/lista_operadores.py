"""
Questões da lista que exigem codificação
"""

"""
Questão 06: Atribua dois valores inteiros as variáveis A e B. Em seguida, utilize a
atribuição múltipla para trocar os valores dessas variáveis.
"""
a = 2
b = 3
print(f'Antes, a: {a}, b: {b}')
a, b = b, a
print(f'Depois, a: {a}, b: {b}')

"""
Questão 07: Construa uma expressão aritmética para encontrar o maior valore, dado 
dois números inteiros. Dica: utilize a função abs() para calcular o valor absoluto.
"""
x = 2
y = 3
z = (x+y+ abs(x-y))//2

"""
Questão 8: Dada as variáveis, informe o tipo de dado que está sendo armazenado
"""
A = 10 #Inteiro
print(type(a))
nome = 'Renato Hidaka' #String
print(type(nome))
N = A - 4 #Inteiro
print(type(N))
lista = [5, 10, N, nome, '902'] #Lista
print(type(lista))
verifica = N > 7 #Booleano
print(type(verifica))

"""
Questão 9: Refatore o código utilizando a atribuição múltipla
nome = 'Renato'
sobrenome = 'Hidaka'
"""
nome, sobrenome = 'Renato', 'Hidaka'
print(nome + ' ' + sobrenome)

"""
Questão 10: Refatore o código utilizando a atribuição composta
X = 10
Y = 5
X = X ** Y % 3
"""
X = 10
Y = 5
X **= Y
X %= 3
print(X)