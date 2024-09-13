print("funciones version 2")
print("Alvarez David")
# zona de lista tuplas set y diccionario
celulares=["Samsung a52", "Iphone 11", "Chafa"]
miset={"manzana", "banana", "mango"}
midiccionario={
  "marca": "Ford",
  "electrico": False,
  "año": 1964,
  "colores": ["rojo", "blanco", "azul"]
} 
# aqui se escriben las funciones
def verlista(telefono):
 for uncelular in telefono:
    print(uncelular)
def verset(elset):
    for unset in elset:
        print(unset)
def verdicc(eldicc):
    for undicc in eldicc:
        print(undicc)
# llamadas a funcion
print("Imprime celulares")
verlista(celulares)
print("Imprime frutas")
verset(miset)
print("imprime carro")
verdicc(midiccionario)
