"""
Faca um programa que, dadas duas listas do mesmo tamanho, imprima o produto escalar entre elas.
Produto escalar e a soma do resultado da multiplicacao entre o numero na posicao i da lista 1 
pelo numero na posicao i da lista 2, com i variando de 0 ao tamanho da lista.
"""

lista_one = [0, 2, 4, 6, 8]
lista_two = [1, 3, 5, 7, 9]
produtoEscalar = 0

for i in range(len(lista_one)):
    print("Multiplicacao dos Indexes: ", i," ( ",lista_one[i], "*",lista_two[i], ")", lista_one[i] * lista_two[i])
    produtoEscalar += lista_one[i] * lista_two[i]

print(produtoEscalar)

### outra forma
pares, impares = list(range(0, 10, 2)), list(range(1, 10, 2))
print(f'O produto escalar entre {pares} e {impares} e {sum([a * b for a, b in zip(pares, impares)])}.')

### outra forma
def escalar(lst1, lst2):
    z = 0
    for i in range(len(lst1)):
        k = lst1[i] * lst2[i]
        z += k
    return z

x = [0, 2, 4, 6, 8]
y = [1, 3, 5, 7, 9]

print(escalar(x, y))

#outra forma 
tamanho = input('Informe o tamanho das listas').split(',')
lista1 = list(map(float, tamanho))
lista2 = list(map(float, tamanho))
print(f'{sum([a * b for a, b in zip(lista1, lista2)])}')
