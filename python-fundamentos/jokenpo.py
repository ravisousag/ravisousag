from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('O computador escolheu {}'.format(itens[computador]))

print(''' 

Suas opções:
0 - Pedra
1 - Papel
2 - Tesoura
''')
jogador = int(input('Insira sua jogada: '))
print ('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

if jogador == computador:
    print('-='*20)
    print('O computador escolheu {} e o jogador {}, então empatou'.format(itens[computador],itens[jogador]))
    print('-='*20)
elif jogador == 0 and computador == 1:
    print('-='*20)
    print('O computador escolheu {} e o jogador {}, então computador ganhou'.format(itens[computador],itens[jogador]))
    print('-='*20)
elif jogador == 0 and computador == 2:
    print('-='*20)
    print('O computador escolheu {} e o jogador {}, então jogador ganhou'.format(itens[computador],itens[jogador]))
    print('-='*20)
elif jogador == 1 and computador == 0:
    print('-='*20)
    print('O computador escolheu {} e o jogador {}, então jogador ganhou'.format(itens[computador],itens[jogador]))
    print('-='*20)
elif jogador == 1 and computador == 2:
    print('-='*20)
    print('O computador escolheu {} e o jogador {}, então computador ganhou'.format(itens[computador],itens[jogador]))
    print('-='*20)
elif jogador == 2 and computador == 0:
    print('-='*20)
    print('O computador escolheu {} e o jogador {}, então computador ganhou'.format(itens[computador],itens[jogador]))
    print('-='*20)
elif jogador == 2 and computador == 1:
    print('-='*20)
    print('O computador escolheu {} e o jogador {}, então Jogador ganhou'.format(itens[computador],itens[jogador]))
    print('-='*20)
else:
   print('-='*20)
   print('JOGADA INVÁLIDA')
   print('-='*20)