

# Input = Permite ingresar una cadena por consola. Asimismo permite brindar una cadena que se mostrara en consola y
# alamacena la cadena ingresada por consola.

palabra = input("INGRESA UNA PALABRA: ")

print("La palabra ingresada es: " + palabra)


# TRANSFORMACION DE CADENAS A DATOS NUMERICOS

#   CADENA a ENTERO
    # int = Permite transformar una cadena a un dato numerico de tipo entero.
    # OJO, ERROR, si usas datos que no son parte de la Funcion "int".

print("\n\tCADENA a ENTERO")
cadena = int(input("Ingrese un Numero: "))
total = cadena + 100
print( cadena, "+ 100 = ", total)


# CADENA a DECIMAL (Numero Flotante)
    # float = Permite transformar una cadena a un dato numerico de tipo flotante o decimal.
    # OJO, ERROR, si usas datos que no son parte de la Funcion "float".

print("\n\tCADENA a DECIMAL (Numero Flotante)")
cadena2 = float(input("Ingrese un numero: "))
tatal2 = cadena2 + 10.5
print(cadena2, " + 10.5 = ", tatal2)