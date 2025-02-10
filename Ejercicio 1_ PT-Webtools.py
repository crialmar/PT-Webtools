''' 🔹 Ejercicio 1: Python
Escribe una función en Python que reciba una lista de números y 
devuelva otra lista con los números duplicados eliminados, manteniendo el orden original.
📌 Ejemplo:'''

entrada = [3, 5, 2, 3, 8, 5, 2, 10]

numbers_duplicated = []

for n in entrada:
    if n not in numbers_duplicated:
        numbers_duplicated.append(n)
print(numbers_duplicated)

salida = [3, 5, 2, 8, 10]
