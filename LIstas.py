# LA FUNCIÓN len()
    # toma el nombre de la lista como un argumento y devuelve el número de elementos almacenados actualmente

Numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", Numeros)           # Imprimiendo el contenido de la lista original.

Numeros[0] = 111
print("\nContenido de la lista con cambio:", Numeros)       # Imprimiendo contenido de la lista con 111.

Numeros[1] = Numeros[4]                                     # Copiando el valor del quinto elemento al segundo elemento.
print("\nContenido de la lista con intercambio:", Numeros)    # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(Numeros))              # Imprimiendo la longitud de la lista.

# =============================================================================================================================

# LA SENTENCIA del
    # Es una Instrucción de eliminar un valor dentro de la lista

del Numeros[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(Numeros))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", Numeros)  # Imprimiendo el contenido de la lista actual.

# =============================================================================================================================

# LA FUNCIÓN clear()
    # Es una Instrucción de eliminar todos los valores de la lista

lista = [8,32,1,23,45,6,7]

print("Longitud de la nueva lista:", len(lista))  # Imprimiendo nueva longitud de la lista.
print("Mi lista: ", lista)
print("\nLista Borrada:", lista.clear())     # Imprimiendo la lista vacía.

# =============================================================================================================================

# EJMEPLO N°1
    # Paso 1: escribe una línea de código que solicite al usuario
    # reemplazar el número de en medio con un número entero ingresado por el usuario.
    # Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
    # Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.


dato = int(input("Ingrese un numero a remplazar: "))

hat_list[2] = dato

del hat_list[4]

print (hat_list)
print("La longitud de la lista es: ", len(hat_list))

# =============================================================================================================================

# MÉTODO append() e insert( , )

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

numbers.append(4)           # El Método "append(valor)" inserta un dato al final de la lista.

print(len(numbers))
print(numbers)

numbers.insert(0, 222)      # El Método "insert(posición,valor)" inserta una dato en la posición escogida
print(len(numbers))
print(numbers)

numbers.insert(1, 333)
print(len(numbers))
print(numbers)

