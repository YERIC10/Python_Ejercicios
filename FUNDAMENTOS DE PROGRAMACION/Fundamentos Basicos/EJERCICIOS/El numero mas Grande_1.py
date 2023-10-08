# Se leen tres números.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable num_grande

num_grande = max(num1, num2, num3)

# Imprime el resultado.
print("El número más grande es:", num_grande)