"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

Quando for criar uma variavel para coisas que não vão mudar
utilizar só letras maiusculas para indicar aos devs que é constante

Tente evitar fazer if muito complexos , linhas muito complexas 
pense em formas de simplificar o código.

"Melhor um código simples do que um complexo"
"""

velocidade = 61  # Velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_Passo_Radar_1 = velocidade > RADAR_1
Carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_1)
local_carro <= (LOCAL_1+RADAR_RANGE)
carro_multado_radar_1 = Carro_passou_radar_1 and velocidade_Passo_Radar_1

if velocidade_Passo_Radar_1:
    print('Velocidade carro passo do radar 1.')

if Carro_passou_radar_1:
    print('carrou passou radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1.')
