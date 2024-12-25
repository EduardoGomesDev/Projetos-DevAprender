# Desafio 1:
'''
Monte um mini-game turtle, que possibilite que o usuário controle para qual direção a tartaruga deve andar(frente/trás) e qual ângulo deverá ser tomado a cada nova movimentação
'''

# Desafio 2:
'''
Usando o mini-game, desenha um quadrado passando instruções para a turtle, totalmente através do input do usuário
'''
from turtle import Turtle

# Inicializando o game da tartaruga
tartaruga = Turtle()

# Definir a velocidade
tartaruga.speed(2)

print('##### Mini-Game Turtle #####')

# Iniciando o laço de repetição (while)
while True:
    # Movimentando a tartaruga para frente
    direcao = input('Para qual direção devemos ir? [f] para frente ou [t] para trás: ')
    if direcao == 'f':
        distancia = int(input('Quantos pixels devemos movimentar para a frente? '))
        print('Você deseja rotacionar a turtle?')
        rotacao = input('Clique [d] para a direira, [e] para a esquerda e [n] para não rotacionar: ')
        if rotacao == 'd':
            angulo = int(input('Quanto para a direita devemos rotacionar? '))
            tartaruga.right(angulo)
        elif rotacao == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar? '))
            tartaruga.left(angulo)
        tartaruga.forward(distancia)       
    # Movimentando a tartaruga para trás
    if direcao == 't':
        distancia = int(input('Quantos pixels devemos movimentar para trás? '))
        rotacao = input('Clique [d] para a direira, [e] para a esquerda e [n] para não rotacionar: ')
        if rotacao == 'd':
            angulo = int(input('Quanto para a direita devemos rotacionar? '))
            tartaruga.right(angulo)
        elif rotacao == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar? '))
            tartaruga.left(angulo)
        tartaruga.backward(distancia)
    resposta = input('Continuar andando? ')
    if resposta not in ('sim', 's'):
        break
print('Jogo finalizado!')