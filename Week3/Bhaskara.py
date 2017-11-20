# Exercício 2 - Desafio da videoaula

#Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.

#O programa deve receber os parâmetros a, b, e c da equação ax2+bx+c, respectivamente, e imprimir o resultado na saída da seguinte maneira:

#Quando não houver raízes reais imprima:

#esta equação não possui raízes reais

#Quando houver apenas uma raiz real imprima:

#a raiz desta equação é X

#onde X é o valor da raiz

#Quando houver duas raízes reais imprima:

#as raízes da equação são X e Y

#onde X e Y são os valor das raízes.

#Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente, ou seja, X deve ser menor que Y.



import math

a = int(input("Digite o valor para a: "))
b = int(input("Digite o valor para b: "))
c = int(input("Digite o valor para c: "))

delta = (b**2) - (4 * (a*c))

if delta < 0:
    print("Esta equação não possui raízes reais")
else:
    if delta == 0:
        x1 = ((b*-1) + math.sqrt(delta)) / (2*a)
        print("A raiz desta equação é X =", x1)
    else:
        x1 = ((b*-1) + math.sqrt(delta)) / (2*a)
        x2 = ((b*-1) - math.sqrt(delta)) / (2*a)
        if  (x1 < x2):
            print("As raízes da equação são: ", x1, "e", x2) #identação
        else:
            print("As raízes da equação são: ", x2, "e", x1) #identação






