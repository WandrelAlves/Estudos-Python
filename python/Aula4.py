# Tipos int e float
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo.

from typing import Self


print(11) # int
print(-11) # int
print(0)

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante.
# float sem sinal é considerado positivo.
print(1.1, 10.11)
print(0.0, -1.5)

# A função type mostra o tipo que o Python
# inferiu ao valor.
print(type("Otávio"))
print(type(1))
print(type(0.1),type(-1.1))


# Evitar a repetição do x e y nas defs então utlizamos o self
class TestMath:

    def __init__(self):
        self.x = 10
        self.y = 10

    def test_add(self):
        return self.x + self.y

