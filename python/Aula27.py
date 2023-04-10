"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'olá mundo'
print(variavel[4:])
print(len(variavel))  # Len motra o tamanho
print(variavel[0:9:2])  # Vai do caractere 0 até o 9 e pulando de 2 em 2
print(variavel[-1:-10:-1]) # o negativo para pegar a string da direita pra equerda



