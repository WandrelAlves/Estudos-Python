"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
lista[2] = 300  # Pode estar alterando esse falor , dps dessa linha
del lista[2]  # Ele acaba apagando a possição do 2 da lista ficando [10,20,40]
# Não muito interressante tirar coisas deuma lista muito grande
# ex lista de 10 mil, vc tirar a segunda vai demorar para alocar todas as posições
# interressante tirar e colocar no final da lista

lista.append(50)  # Adicionar na lista
lista.pop()  # retira o ultimo valor da lista, retira o 50 nesse momento e dps adiciona o 60
lista.append(60)
lista.append('BBB')
ultimo_valor = lista.pop()
print(lista, 'Removido,', ultimo_valor)
