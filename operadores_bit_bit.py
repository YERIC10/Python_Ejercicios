print("============================")
print("OPERADORES LOGICOS Y DE BITS")
print("============================\n")

v1 = int(input("Ingrese primer valor: "))
v2 = int(input("Ingrese segundo valor: "))

print("\nOPERADORES LOGICOS")
print("------------------\n")
print("Operador Logico 'and' - CONJUNCION ")    # Operador Lógico 'Y' CONJUNCIÓN LOGICA
print(v1, " > 0 and ", v2, " > 10 \n", v1 > 0 and v2 > 10, "\n")

print("Operador Logico 'or' - DISYUNCION")      # Operador Lógico 'O' DISYUNCIÓN LOGICA
print(v1, " > 0 or ", v2, " > 10 \n", v1 > 0 or v2 > 10, "\n")

print("Operador Logico 'not' - NEGACION")       # Operador Lógico 'No' NEGACIÓN LOGICA
print("not ", v1, " == ", v2, "\n", not v1 == v2)

print("\nOPERADORES BINARIOS")
print("-------------------\n")

print("Operador Bit '&' CONJUNCION")                    # Operador Bit 'Y' CONJUNCIÓN BINARIA
print(v1, " & ", v2, " = ", v1 & v2)                    # 0 & 0 = 0         0 & 1 = 0
print(bin(v1), " & ", bin(v2), " = ", bin(v1 & v2))     # 1 & 0 = 0         1 & 1 = 1  OJO: El 0 es prioridad

print("\nOperador Bit '|' DISYUNCION")                   # Operador Bit 'O' DISYUNCIÓN BINARIA
print(v1, " | ", v2, " = ", v1 | v2)                     # 0 & 0 = 0         0 & 1 = 1
print(bin(v1), " | ", bin(v2), " = ", bin(v1 | v2))      # 1 & 0 = 1         1 & 1 = 1  OJO: El 1 es prioridad

print("\nOperador Bit '~' NEGACION")                                            # Operador Bit '~' NEGACIÓN BINARIA
print("~", v1, " = ", ~v1, " and ", "~", v2, " = ", ~v2)                        # OJO: NO es la inversa de los bits del número,
print("~", bin(v1), " = ", bin(~v1), " and ", "~", bin(v2), " = ", bin(~v2))    # es la suma de un bit al resultado
                                                                                  # EJEMPLO: 5 = 0101 => ~5 = 0101 + 1
                                                                                  #                   => ~5 = 0110
                                                                                  #                   => ~5 = -6

print("\nOperador Bit '^' EXCLUSION")                   # Operador Bit '^' EXCLUSIÓN BINARIA
print(v1, " ^ ", v2, " = ", v1 ^ v2)                    # 0 & 0 = 0         0 & 1 = 1
print(bin(v1), " ^ ", bin(v2), " = ", bin(v1 ^ v2))     # 1 & 0 = 1         1 & 1 = 0  OJO: tanto 1 y 0 son de prioridad

print("\nDESPLAZAMIENTO A LA DERECHA")
print("---------------------------\n")

numero = 15                                     # 15 = 1111
resultado = numero >> 3                         # >> 3 : CANTIDAD DE BITS QUE SE DESPLAZARAN HACIA LA DERECHA
print("numero >> 2 = ", resultado)              # 1111 << 3: SE DESPLAZA 3 BITS HACIA LA DERECHA = 0001 = 1
print(bin(numero), ">> 2 = ", bin(resultado))   # CALCULO: 15 / 2^(3) donde 3 es la cantidad de bits de desplazamiento

print("\nDESPLAZAMIENTO A LA IZQUIERDA")
print("---------------------------\n")

numero = 20  # 20 = 10100
resultado = numero << 3                         # >> 3 : CANTIDAD DE BITS QUE SE DESPLAZARAN HACIA LA IZQUIERDA
print("numero << 3 = ", resultado)              # 10100 << 3: SE DESPLAZA 3 BITS HACIA LA DERECHA = 10100000 = 160
print(bin(numero), "<< 3 = ", bin(resultado))   # CALCULO: 20 x 2^(3), donde 3 es la cantidad de bits de desplazamiento
