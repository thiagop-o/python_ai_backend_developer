nome = "tHIagO"

print(nome.upper()) #tudo maiuscula
print(nome.lower()) #tudo minuscula
print(nome.title()) #primeira maiuscula

texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".") #remove espaços
print(texto.rstrip() + ".") #right strip, remove espaços da direita
print(texto.lstrip() + ".") #left strip, remove espaços da esquerda

menu = "Python"

print("####" + menu + "####")
print(menu.center(14)) #centraliza entre 14 caracteres
print(menu.center(14, "#")) #centraliza e adiciona # ate dar 14 caracteres
print("-".join(menu)) #mescla cada letra com o caracter