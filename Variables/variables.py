
# Variables en Python

a = 3
b = 7

c = a + b

print(c)

# Definiendo una variable

nombre = "Anselmo"

# Redefiniendo una variable

nombre = "Luis"

nombre += " Del Hoyo"

print(nombre)

# Concatenación

bienvenida = "Hola! " + nombre + " ¿cómo estás?" # No admite números

dni = 16873516

bienvenida_dni = f"Hola! {dni} ¿cómo estás?" # El fstring transforma todo a string

print(bienvenida)
print(bienvenida_dni)

# Operadores de pertenencia (in y not in)

print("Luis" in bienvenida)
print("Luis" not in bienvenida)