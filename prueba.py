

lista_1 = [1,3,5,7,9]
lista_2 = [2,4,6,8,10]

lista_1[1], lista_1[2], lista_1[3], lista_1[4], lista_2[0], lista_2[1], lista_2[2], lista_2[3] = \
    lista_2[0], lista_1[1], lista_2[1], lista_1[2], lista_2[2], lista_1[3], lista_2[3], lista_1[4]

lista_tot = []
long = len(lista_1)
lista_tot = lista_1 + lista_2

print(lista_1)
print(lista_2)
print(lista_tot)