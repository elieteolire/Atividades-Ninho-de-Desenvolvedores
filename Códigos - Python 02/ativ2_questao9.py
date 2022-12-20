#Escreva um programa Python para contar as ocorrências de cada palavra em uma determinada frase.

print("A frase que terá suas palavras contadas → O céu é azul.")
palavras_contadas = {'o', 'céu', 'é', 'azul'}

texto = ['o', 'céu', 'é', 'azul']
dicionario = {}
for palavra in texto:
    if palavra in palavras_contadas:
        count = 1
        if palavra in dicionario:
          count = int(dicionario[palavra].split(' ')[-1]) + 1;
        dicionario[palavra] = palavra + " " + str(count)

for palavra in palavras_contadas:
  if palavra not in texto:
    dicionario[palavra] = palavra + " " + str(0)

for chave in dicionario:
    print (dicionario[chave])