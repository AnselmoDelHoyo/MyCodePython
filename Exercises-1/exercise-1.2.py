
# Ejercicio 2

# a) Pedirle al usuario que diga cualquier texto real y:

# - calcular cuanto tardaría en decir esa frase.
# - ¿Cuántas palabras dijo?

promedio_palabra = 2

texto_usuario = input("Escribe un texto: ")

palabras = texto_usuario.split(" ")

print(f"El usuario tarda { len(palabras) * promedio_palabra } segundos en decir la frase.")
print(f"El usuario dijo { len(palabras) } palabras.")

# b) Si se tarde más de 1 minuto:

# - decirle: "para flaco tampoco te pedí un testamento"

if (len(palabras) > 120) :
    print("Para flaco, tampoco te pedí un testamento.")

# c) Dalto habla un 30% más rápido: ¿cuánto tardaría él en decirlo?

print(f"Dalto tardaría { len(palabras) * promedio_palabra - ((len(palabras) * promedio_palabra) * 30 / 100) } segundos en decir la frase.")