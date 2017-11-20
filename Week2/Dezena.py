#Entrada de Dados:
#Digite um número inteiro: 78615

#Saída de Dados:
#O dígito das dezenas é 1

#Exemplo 2:

#Entrada de Dados:
#Digite um número inteiro: 2

#Saída de Dados:
#O dígito das dezenas é 0

n = int(input("Digite um número inteiro: "))
d = (n // 10) % 10

print("O dígito das dezenas é ", d)


