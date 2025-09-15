
# Métodos de diccionarios

diccionario = {
    "nombre" : "Anselmo",
    "apellido" : "Del Hoyo",
    "edad" : 19
}

# keys() -> devuelve las claves
claves = diccionario.keys()

# get() -> devuelve el valor de una clave
valor = diccionario.get("nombre")

# clear() -> elimina todos los elementos
# diccionario.clear()

# pop() -> elimina un elemento
diccionario.pop("nombre")

# items() -> para iterar el dict
diccionario_iterable = diccionario.items()

print(claves)
print(valor)
print(diccionario_iterable)