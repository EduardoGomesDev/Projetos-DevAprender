# Projeto 1

## Objetivo do projeto
# * Estamos criando um módulo de login do nosso app, e você deve obter as seguinter informações do usuário

from datetime import datetime
from random import choice

# Módulo 1
## Funcionalidades do módulo 1

# 1. Obtenha o nome do usuário;
nome_do_usuario = input('Digite seu nome: ').upper().strip()

# 2. Obtenha a idade do usuário;
idade_do_usuario = int(input('Digite sua idade: '))

# 3. Registre de forma automatica a data do cadastro do usuário, usando a data do registro como data de registro.
data_do_cadastro = datetime.now().date()
data_do_registro = data_do_cadastro.strftime('%d/%m/%Y')
# print(data_do_registro)

# 4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
cartoes = ['R$50,00','R$250,00','R$120,00']
cartao_sorteado = choice(cartoes)

# 5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
data_do_aniversario = datetime.strptime(input('Digite a sua próxima data de aniversário: '),'%d/%m/%Y').date()

# Módulo 2
## Funcionalidades do módulo 2 - mensagem de boas vindas

'''
1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).
Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).
'''
print(f'Olá {nome_do_usuario}, seu registro foi conluido com sucesso no dia {data_do_registro}. \nParabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao_sorteado}')