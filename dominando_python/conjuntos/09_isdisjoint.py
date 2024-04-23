conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True Se A nao esta contido em B
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False Se B nao esta contido em A
print(resultado)
