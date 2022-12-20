salario=float (input("Digite o valor do salário: "))
financ=float (input("Digite o valor do financiamento pretendido: "))

if financ<=5*salario:
    print("Financiamento concedido. Obrigada por nos consultar!")
    
else:
    print("Financiamento negado. Obrigada por nos consultar!")