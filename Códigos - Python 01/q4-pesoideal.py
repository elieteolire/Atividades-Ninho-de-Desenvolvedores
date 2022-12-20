g=str(input("Digite o seu gênero: F ou M: "))
a=float(input("Digite sua altura:"))
p=float

if g=="F":
    p=(62.1*a)-44.7
    print("Seu peso ideal é ", p, "quilos.")

elif g=="M":
    p=(72.7*a)-58
    print("Seu peso ideal é ", p, "quilos.")
    
else:
    print("Digite um gênero válido!")
