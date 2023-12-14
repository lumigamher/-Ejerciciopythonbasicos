import random

lista = [0] * 10

for i in range(10):
  lista[i] = random.randint(1, 10) 



def mostrarlista(listaa):
  for i in range(10):
    print(listaa[i])

def ordenascendente(ordenado):
  for i in range(10):
    for j in range(9):
      if ordenado[j] > ordenado[j + 1]:
        aux = ordenado[j]
        ordenado[j] = ordenado[j + 1]  
        ordenado[j + 1] = aux

def ordendescendente(ordenado):
  for i in range(10):
    for j in range(9):
      if ordenado[j] < ordenado[j + 1]:
        aux = ordenado[j]
        ordenado[j] = ordenado[j + 1]
        ordenado[j + 1] = aux

ordenascendente(lista)

print("La lista ascendente:")
mostrarlista(lista)

ordendescendente(lista)  

print("La lista descendente:")
mostrarlista(lista)