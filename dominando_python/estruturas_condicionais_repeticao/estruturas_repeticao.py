nome = input("Informe seu nome: ")
vogais = "AEIOU"

for letras in nome:
    if letras.upper() in vogais:
        print(letras, end="")
else:
    print()
    
for numero in range(0,11):
    print(numero, end=" ")
print()
    
for numero in range(0, 9*10 + 1, 9 ):
    print(numero, end=" ")
print()
    
estado = True
while estado:
    for numero in range(0, 101):
        if numero == 26:
            estado = False
            break

for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")