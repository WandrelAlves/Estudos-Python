Nome = 'Lui Otávio'
altura = 1.80
peso = 95
imc = peso/(altura ** 2)  # IMC = peso / (altura^2)

'f-strings'
linha_1 = f'{Nome} tem {altura:.2f} de altura'
linha_2 = f'pesa, {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
print(imc)
