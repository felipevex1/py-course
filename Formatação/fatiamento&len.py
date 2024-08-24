"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:]) # início no índice 4
print(variavel[0:4]) # início no índice 0 e término no 4
print(variavel[:6]) # O python entende que começa do 0
print(variavel[0:9:1]) # passo de 1 em 1
print(variavel[0:9:2]) # passo de 2
print(variavel[0:9:3]) # passo de 3

print(len(variavel)) # len() checa tamanho da variavel
print(len(variavel[0:3]))

teste = input("Digite algo: ")
print(len(teste))