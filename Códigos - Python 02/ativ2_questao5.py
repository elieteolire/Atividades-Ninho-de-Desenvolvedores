#Escreva um programa em Python para multiplicar todos os itens de uma lista.

def multiplic_lista(lista1):
    result = 1
    for x in lista1:
        result = result * x
    return result
 

lista1 = [3, 6, 9, 12]
print ("O produto dos itens da lista", lista1, "é: ")
print(multiplic_lista(lista1))