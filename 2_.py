# Operaciones con listas

# + podemos unir listas
# * podemos repetir listas
# append nos permite aniadir un elemento a la lista
# sort nos permite ordenar 
# pop nos permite eliminar un elemento de la cola
# del nos permite eliminar determinado indice de la lista
from xml.dom.expatbuilder import FragmentBuilder


a = [1,2]
del a[-1]
print(a)

pares = list(range(0,100,2))
print(pares)

fruit = list()
fruit.append("Manzana")
import random
rando_n = []
for i in range(10):
        rando_n.append(random.randint(0,15))