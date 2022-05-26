"""
Crie o jogo Pedra, Papel, Tesoura' por meio de um código em Python. 
Para isso, solicite que o primeiro jogador informe a sua escolha e o segundo jogador deve ser o computador. 
Por fim, utilize os ifs para saber quem seria o vencedor.
"""

#import 
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''Suas opcoes: 
| 0 | Pedra
| 1 | Papel
| 2 | Tesoura''')
jogador = int(input('Qual sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
if jogador > 2:
    print('Jogada invalida')
else:
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)
    
    if computador == 0: #computador jogou PEDRA
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('Jogador ganhou')
        elif jogador == 2:
            print('Computador ganhou')
    if computador == 1: #computador jogou PAPEL
        if jogador == 0:
            print('Computador ganhou')
        elif jogador == 1:
            print('Empate')
        elif jogador == 2:
            print('Jogador ganhou')
    if computador == 2: #computador jogou TESOURA
        if jogador == 0:
            print('Joagador ganhou')
        elif jogador == 1:
            print('Computador ganhou')
        elif jogador == 2:
            print('Empate')
