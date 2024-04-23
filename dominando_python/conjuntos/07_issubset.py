conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True Se A esta contido em B
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False Se B esta contido em A
print(resultado)
