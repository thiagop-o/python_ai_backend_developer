### OPERADORES ARITMETICOS ###
#Adicao
print(1 + 1)

#Subtracao
print(10 - 2)

#Multiplicacao
print(5 * 3)

#Divisao
print(10 / 2)

#Divisao Inteira
print(10 // 2)

#Modulo
print(10 % 2)

#Exponenciacao
print(2 ** 3)

### OPERADORES DE COMPARACAO ###
#Igualdade
print (1 == 2)

#Diferenca
print (1 != 2)

#Maior ou igual
print (1 >= 2)

#Menor ou igual
print (1 <= 2)

### OPERADORES DE ATRIBUICAO ###
#Atribuicao Simples
variavel = 500

#Atribuicao com Adicao
variavel += 500

#Atribuicao com Subtracao
variavel -= 200

#Atribuicao com Multiplicacao
variavel *= 2

#Atribuicao com Divisao
variavel /= 10

### OPERADORES DE COMPARACAO ###
#E (and)
print(1 > 2 and 2 == 2)

#Ou (or)
print(1 > 2 or 2 == 2)

#Negacao (not)
print(not 1000 > 500) #Lista vazia ou String Vazia em python retorna False

### OPERADORES DE IDENTIDADE ###
#Se esta no mesmo espaco de memoria
curso = "Python"
linguagem = curso

print(curso is linguagem)

### OPERADORES DE ASSOCIACAO ###
#Se esta incluso no objeto
curso = "Curso de Python"
frutas = ["laranja", "maça", "uva"]
linguagem = curso

print("Python" in curso)
print("kiwi" in frutas)