ingreso_mensual = 12000
gasto_mensual = 8000

if ingreso_mensual > 10000:
    print("Estás bien en cualquier parte del mundo.")
    
    if ingreso_mensual - gasto_mensual < 0:
        print("Pero estás en déficit.")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("No deberías gastar más.")
    else:
        print("Estás gastando mucha plata brother, te quedarás pobre.")

elif ingreso_mensual > 1000:
    print("Estás bien en latinoamérica.")

else:
    print("Eres pobre.")