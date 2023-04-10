# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-

nome = 'Otávio'
print(nome[2])
print(nome[-4])
print('vio' in nome)  # condição true
print('zero' in nome)  # condição false
print(10 * '-')
print('vio' not in nome)  # condição não está false
print('zero' not in nome)  # True

nome = input('Digite o seu nome:')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')
