def coordenadaZ(x, y):
    x = x + 10  #16
    y = y + 15  #22
    return print (x + y)    #38, 40, 42

# programa principal
x = int(input("Coordenada eje x: "))    #6
y = int(input("Coordenada eje y: "))    #7
for i in range(3):
    z = coordenadaZ(x, y) #invoca a la funcion coodenadasZ
    x = x + 1   #6 + 3 del range = 9
    y = y + 1   #7 + 3 del range = 10

print(x, " . ", y)

# =============================================================================================================================

# Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club.
# Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento
# mediante el ingreso de un nombre vacío. Precondición: el formato del nombre de los socios será: nombre apellido.
# Podría ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más de un apellido,
# el usuario sólo ingresará uno. Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa
# debe dejar al usuario en un bucle hasta que ingrese un DNI correcto. Por cada socio se debe imprimir su identificador
# único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI.
# Ejemplo:
# Nombre: Alba María Linares
# DNI: 25834910
# Alba7258


nombre1 = input("Ingrese su Primer Nombre: ").title()
nombre2 = input("Ingrese su Segundo Nombre: ").title()
apellido = input("Ingrese su Primer Apellido: ").title()

while True:
    dni = str(input("Ingrese su  Documento Nacional de Identificacion (DNI): "))
    if len(dni) == 8 or len(dni) == 7:
        break
    else:
        print("\tError... Ingrese un DNI VALIDO \n")

id = nombre1 + str(len(apellido)) + str(len(dni[4]))

#DATOS
print("Nombre: " + nombre1 + nombre2 + apellido)
print("DNI: " + dni)
print("ID: " + id)


# =============================================================================================================================


# Crear tu propia Lista emulando Do While. Hallar la suma de todos los valores de tu lista
lista = []
total = 0

while True:
    valor = int(input("Ingrese valores para tu lista, presiona 0 para terminar: "))
    if valor != 0:
        lista.append(valor)
        total += lista
    else:
        break

for i in range(len(lista)):
    total += lista[i]

print("\n")
print("La Longitud  de tu Lista: ", len(lista))
print("Mi Lista: ", lista)
print("La suma de todos los valores de tu Lista: ", total)

