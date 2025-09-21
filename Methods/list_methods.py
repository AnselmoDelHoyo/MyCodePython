
# List methods

lista = list(["Hola", "Luis", 18])
list1 = ["Del", "Add", "More"]
print(list1)

# Devuelve la cantidad de elementos
cantidad_elementos = len(lista)

# Agregando un elemento a la lista
lista.append(1.84)

# Agregando un elemento a la lista en un índice específico
lista.insert(2, "Del Hoyo")

# Agregando varios elementos a al lista
lista.extend(["Cyber security", True])

# Eliminando un elemento de la lista (por su índice)
lista.pop(len(lista) - 1) # Con solo colocar -1 elimina el último.

# Eliminando un elemento de la lista (por su valor)
lista.remove("Hola") # Si el elemento no es encontrado lanza un error.

# Eliminando todos los elementos de la lista
# lista.clear()

# Ordenando elementos de la lista

# No se pueden ordenar elementos de diferente tipo
# lista.sort()

lista2 = [2004, 2021, 1998, True]

# Si usamos el parámetro "reverse=True" invierto el orden de los elementos
lista2.sort(reverse=True)

# Invirtiendo el orden de los elementos
lista.reverse()

# Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(18) 

print(lista)
print(elemento_encontrado)
print(lista2)