#Escreva um programa em Python para somar todos os itens de uma lista.

def soma_itens(lista1):
    l = lista1
    return l

l = soma_itens([3,6,9,12])
soma = 0

for i in range(len(l)):
    soma += l[i]
print("A soma dos itens da lista é: ", soma)