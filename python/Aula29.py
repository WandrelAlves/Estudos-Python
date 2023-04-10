"""
Introdução ao try/expept
try -> tentar executar ocódigo
except => ocorreu algum ao tentar executar
"""


# Tudo que user informar tem que ser tratado
# Caso fosse feito numero_str(2) * 2 seria = 22 e não 4

numero_str = input('Vou dobrar o número digitado: ')

"""
Nesse caso o try é para que o Python tente executar aquele código e caso não consiga 
executar por conta de um erro ele vai retornar o que temos dentro do except.

# Quando vc tenta converter a str não conseguir converter e já vai pular pro except.
# Para tentar capturar o erro de uma forma mais rapida.

"""

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')

except:
    print('Isso não é um número.')
