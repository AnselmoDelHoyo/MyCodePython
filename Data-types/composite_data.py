
# La lista

lista = ["Anselmo", "Del Hoyo", True, 1.82]

# La tupla no se puede modificar, la lista sí.

tupla = ("Anselmo", "Del Hoyo", True, 1.82)

lista[0] = "Luis"

print(lista[1])
print(tupla[1])

# Creando un conjunto (set)

# El conjunto es parecido a la tupla
# El conjunto no acepta valores repetidos
# Se accede a sus valores con un bucle
# Sus valores son desordenados

conjunto = {"Anselmo", "Del Hoyo", True, 1.82, "Del Hoyo"}

print(conjunto)

# Creando un diccionario

diccionario = {
    # key : Value,
    "nombre": "Anselmo Del Hoyo",
    "canal": "ADH11",
    "es_desarrollador": True,
    "altura": 1.82,
    "nombre_duplicado": "Anselmo Del Hoyo"
}

print(diccionario["altura"])
print(tupla[3])