def meu_gerador(numeros: list[int]):
    for index, numero in enumerate(numeros):
        print(index)
        yield numero * 2 # geradores utilizam yield no lugar de return para economizar memoria


for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)
