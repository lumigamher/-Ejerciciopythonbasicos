a = 270
b = 340 
c = 390

# Monedas de 10, 50 y 100 para dar vueltos

print("Escoja el producto: ")
print("A vale $270")
print("B vale $340") 
print("C vale $390")

prod = input("Producto: ") # Leer producto



def cambio(x):
  smoneda = 0
  while smoneda <= x:
    print("Ingrese las monedas: ")
    print("La maquina solo recibe monedas de $10 $50 o $100")  
    moneda = int(input("Moneda: ")) 
    if moneda == 10 or moneda == 50 or moneda == 100:
      smoneda = smoneda + moneda
    else:
      print("La moneda ingresada sera devuelva, ingrese una denominación correcta.")

  vueltos = smoneda - x  
  while vueltos > 0:
    if vueltos >= 50:
      print("Su cambio es: $50")
      vueltos = vueltos - 50
    elif vueltos < 50:
      print("Su cambio es $10") 
      vueltos = vueltos - 10

if prod == "a":
  cambio(a)
elif prod == "b":
  cambio(b)  
elif prod == "c":
  cambio(c)