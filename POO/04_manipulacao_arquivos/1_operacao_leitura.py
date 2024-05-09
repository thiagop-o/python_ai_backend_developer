# arquivo = open(
#     "POO/04_manipulacao_arquivos/lorem.txt", "r"
# )
# print(arquivo.read())
# arquivo.close()

# arquivo = open(
#     "POO/04_manipulacao_arquivos/lorem.txt", "r"
# )
# print(arquivo.readline())
# arquivo.close()

# arquivo = open(
#     "POO/04_manipulacao_arquivos/lorem.txt", "r"
# )
# print(arquivo.readlines())
# arquivo.close()

arquivo = open(
    "POO/04_manipulacao_arquivos/lorem.txt", "r"
)
# tip
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()
