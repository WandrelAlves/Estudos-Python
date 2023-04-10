"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# 1)
numero = input("Digite um número: ")


if numero.isdigit():
    resultado = numero % 2 == 0

    if resultado:
        print('Numero par!')

    else:
        print('Numero impár!')

else:
    print('Você não digitou um número inteiro')

# 2)

Horas = int(input('Digite as horas: '))

try:

    if Horas <= 11 and Horas >= 00:
        print('Bom dia!')
    elif Horas >= 12 and Horas <= 17:
        print('Boa tarde!')
    elif Horas >= 18 and Horas <= 23:
        print('Boa noite!')
    else:
        print('Horário desconhecido.')
except:
    print('Você não digitou nenhum número inteiro!')

# 3)

Nome = input("digite nome: ")

contagem = len(Nome)

NomeCurto = contagem <= 5
NomeMedio = contagem == 6
NomeLongo = contagem > 6

if NomeCurto:
    print('Seu nome é curto')
elif NomeMedio:
    print('Seu nome é normal')
else:
    print('Seu nome é longo')
