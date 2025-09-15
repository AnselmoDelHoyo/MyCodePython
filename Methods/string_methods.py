
# String methods

cadena1 = "Hola soy Anselmo"
cadena2 = "Bienvenido crack"

# DIR - devuelve la lista de atributos válidos del objeto pasado.
dir_cadena = dir(cadena1)

# UPPER - convierte a mayúscula.
upper_cadena = cadena1.upper()

# LOWER - convierte a minúscula.
upper_cadena = cadena1.lower()

# CAPITALIZE - primera en mayúscula.
upper_cadena = cadena1.capitalize()

# FIND - método encuentra la primera aparición del valor especificado, sino devuelve 1.
find_cadena = cadena2.find("B")

# INDEX - método encuentra la primera aparición del valor especificado, sino devuelve una excepción.
index_cadena = cadena2.index("B")

# ISNUMERIC - si es numérico devuelve true.
is_numeric_cadena = "3242110".isnumeric()

# ISALPHA - si es alfa numérico devuelve true.
is_alpha_cadena = "sABEtEr".isalpha()

# COUNT - devuelve el número de ocurrencias de una subcadena en la cadena dada.
count_cadena = cadena1.count("o")

# LEN - cuenta los caracteres de una cadena.
len_cadena = len(cadena1)

# ENDSWITH - verifica si una cadena termina con.
endswith_cadena = cadena2.endswith("k")

# STARTSWITH - verifica si una cadena comienza con.
startswith_cadena = cadena2.startswith("B")

# REPLACE - reemplaza un valor por otro.
replace_cadena = cadena1.replace("soy", "me llamo")

# SPLIT - separa por el parámetro dado.
split_cadena = cadena1.split("o")

print(split_cadena)