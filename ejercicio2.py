print("Escriba cuantos dias: ")
n = int(input())

dolar = [0] * (n+1) 

for i in range(1, n+1):
  print("Dia: ", i)
  print("Ingrese el precio del Dolar: ")
  dolari = float(input())
  dolar[i] = dolari

my = 0
alza = [0] * (n+1)

for i in range(1, n):
  dif = dolar[i+1]-dolar[i]
  alza[i] = dif
  
  if alza[i] > my:
    my = alza[i]

print("La mayor alza de los dias ingresados es: ", my)