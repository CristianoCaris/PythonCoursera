#Entrada de Dados:
#Por favor, entre com o número de segundos que deseja converter: 178615

#Saída de Dados:
#2 dias, 1 horas, 36 minutos e 55 segundos.

segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos_int = int(segundos_str)

dias = segundos_int // 86400
segundos_int = segundos_int % 86400

horas = segundos_int // 3600
segundos_int = segundos_int % 3600

minutos = segundos_int // 60
segundos_int = segundos_int % 60

print (dias," dias,", horas, " horas,", minutos, " minutos e ", segundos_int, " segundos.")


