#Escreva uma função Python que receba uma lista de palavras e retorne o comprimento da mais longa.

frase = input('Digite uma frase: ').split()
tamanho_palavras = list()
for palavra in frase:
    tamanho_palavras.append(len(palavra))

maior = max(tamanho_palavras)
print("A maior palavra da frase é: ")
for a, b in zip(frase, tamanho_palavras):
    if b == maior:
        print(a)