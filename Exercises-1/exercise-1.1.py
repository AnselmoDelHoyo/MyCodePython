
# Ejercicio 1

# a) Diferencia en porcentaje entre el curso actual y:

# - el más rápido de otros cursos.
# - el más lento de otros cursos.
# - el promedio de los cursos.

print("--------------------")

curso_rapido = 2.5
curso_lento = 7
curso_promedio = 4
curso_actual = 1.5

diferencia_actual_rapido = 100 - curso_actual * 100 // curso_rapido
diferencia_actual_lento = 100 - curso_actual * 100 // curso_lento
diferencia_actual_promedio = 100 - curso_actual * 100 // curso_promedio

print(f"El curso actual es {diferencia_actual_rapido}% más rápido que el curso rápido.")
print(f"El curso actual es {diferencia_actual_lento}% más rápido que el curso lento.")
print(f"El curso actual es {diferencia_actual_promedio}% más rápido que el curso promedio.")




# b) Porcentaje de material inservible que se reduce en:

# - el promedio de los cursos.
# - el curso actual (este curso).

print("--------------------")

curso_promedio_crudo = 5
curso_actual_crudo = 3.5

material_inservible_promedio = 100 - (curso_promedio * 100 // curso_promedio_crudo)
material_inservible_actual = 100 - (curso_actual * 100 // curso_actual_crudo)

print(f"El porcentaje de material inservible que se reduce en el promedio de los cursos es de {material_inservible_promedio}%")
print(f"El porcentaje de material inservible que se reduce en el curso actual es de {material_inservible_actual}%")

# c) ¿Ver 10 horas de este curso a cuántas de otros cursos equivale?

print("--------------------")

print(f"Ver 10 horas de este curso equivale a ver {curso_promedio * 100 // curso_actual / 10} horas de otros cursos.")
print(f"Ver 10 horas de otros cursos equivale a ver {curso_actual * 100 // curso_promedio / 10} horas de otros cursos.")
