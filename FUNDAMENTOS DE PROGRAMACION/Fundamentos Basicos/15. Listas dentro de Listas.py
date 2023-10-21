# Listas dentro de listas

# Ejemplo 1
board = []                          # Lista Principal

for i in range(8):                  # Un bucle donde se ejecuta 8 veces
    row = [i for i in range(8)]     # raw, es una Lista de Filas con datos de 0 - (8-1)
    board.append(row)               # la lista raw se almacena en la lista principal board

print(board)


# Ejemplo 1
board = [[i for i in range(8)] for j in range(8)]   # Esto es lo mismo que el anterior pero con una sola lista y mas definida
     #  i = [0 - 7]
print(board)

