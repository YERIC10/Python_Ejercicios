def anio_bisiesto(anio, respuesta):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        if respuesta == "SI":
            print(f"CORRECTO, {anio} es un Año Biciesto")
        else:
            print(f"FALLIDO, {anio} si es un Año Biciesto")

    else:
        if respuesta == "SI":
            print(f"FALLIDO, {anio} no es un Año Biciesto")
        else:
            print(f"CORRECTO {anio} no es un Año Biciesto")

while True:
    Anio = int(input("Ingrese un año: "))
    if (Anio >= 1000 and Anio <= 9999):
        break
    else:
        print("\n No es un Año correcto")

while True:
    Respuesta = str(input(f"¿El año {Anio} es Bisiesto? (Si/No): "))
    valores = ["SI", "NO"]
    resp = list(Respuesta.upper())         # Transformamos a mayuscula la Respuesta y lo convertimos en una lista que se va almacenar en resp
    Respuesta = ''.join(resp[0:2])      # Funcion join(), trasforma el contenido de una lista en una palabra
    if (Respuesta == valores[0]) or (Respuesta == valores[1]):
        break
    else:
        print("\nNo es una palabra correcta")

anio_bisiesto(Anio, Respuesta)