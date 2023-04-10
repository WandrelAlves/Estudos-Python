"""
while/else

Não muito util
"""

string = 'Valor qualquer'


i = 0
while i< len(string):
    letra = string[i]

    if letra == ' ':
        break

    # break  O else n executa com o break

    print(letra)
    i += 1

else:
    print('Não encontrei espaço na string')
print('Fora do while')





