n = int(input("Ingrese un numero entero mayor a 0: "))
pasos = 0

while (n > 0 and n != 1):

    if (n % 2 == 0):
        n /= 2
    else:
        n = (3 * n) + 1

    pasos += 1
    print(n)

print("pasos " + str(pasos))