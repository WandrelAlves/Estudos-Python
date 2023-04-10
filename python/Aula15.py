# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')


nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')
#  ou
# print(f'O seu nome é {nome=}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

# Serve pra fazer uma checagem para que o código não quebre nas linhas acima
# Caso aconteça não tem como checar para ver qual é o erro
# Então ele quebra nas linhas a abaixo fazendo com que possamos verificar o erro

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos número é: {int_numero_1 + int_numero_2}')
