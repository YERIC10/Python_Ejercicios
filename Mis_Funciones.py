# FUNCIONES DEFINIDAS

def raiz_cubica(raiz):  # def = Define la creación de Funciones
    result = raiz ** 1 / 3
    return print(result)


raiz_cubica(5)


# _____________________________________________________________________________________

#  *args

def suma_varios(*args):  # *args = puede almacenar una lista de parámetros
    result = 0
    for i in args:
        result += i
    return print(result)


suma_varios(3, 5, 6, 7, 8, 9, 10)

# _____________________________________________________________________________________

# FUNCIONES RECURSIVAS

def funci_recursiva(num):  # Son funciones que se llaman asi misma dentro de ella


    if num > 0:
        print(num)
        funci_recursiva(num - 1)

funci_recursiva(3)

# _____________________________________________________________________________________

# FUNCIONES LAMBDA
# Son funciones más resumida realizadas en una sola línea de código
result = lambda a, b, c: (a ** b) + c  # La función Lambda ocupa menos espacio de memoria
print(result(1, 2, 4))  # a,b,c: = son los parámetros de la función Lambda
# : (a**b) + c = es la operación que se vá realizar dentro de la función
