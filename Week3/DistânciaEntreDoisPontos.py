#Receba 4 números inteiros na entrada. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

#Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

#longe

#na saída. Caso o contrário, quando a distância for menor que 10, imprima

#perto

import math

x1 = int(input("Digite X1: "))
y1 = int(input("Digite Y1: "))
x2 = int(input("Digite X2: "))
y2 = int(input("Digite Y2: "))

x = (x2-x1)**2
y = (y2-y1)**2


d = math.sqrt(x + y)

if (d >= 10):
    print("Longe")
else:
    print("Perto")
