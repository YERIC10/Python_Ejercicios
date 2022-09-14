bloques = int(input("Ingrese el número de bloques:"))

altura = 0
nivel = 1
while altura < bloques:
    bloques -= nivel
    altura += 1
    nivel += 1


else:

    print("La altura de la pirámide:", altura)