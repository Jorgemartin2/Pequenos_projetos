from random import randint
from time import sleep
from emoji import emojize
jogador_vence=computador_vence=empate=0
jogar='S'
print('-=-=-=-=-\033[35;45m JOKENPO \033[m-=-=-=-=-')
while jogar == 'S':
    opcoes=('Pedra','Papel','Tesoura')
    computador=randint(0,2)
    print(emojize('''Escolha sua jogada:
    [0] PEDRA:raised_fist:
    [1] PAPEL:raised_hand:
    [2] TESOURA:victory_hand:'''))
    jogadas=[0,1,2]
    jogador=int(input('Qual é a sua jogada?'))
    while jogador not in jogadas:
        jogador=int(input('Jogada inválida. Digite um valor válido [0, 1, 2]. Qual é a sua jogada?'))
    print('\033[35mJO\033[35m')
    sleep(1)
    print('\033[35mKEN\033[m')
    sleep(1)
    print('\033[35mPO\033[m') 
    print(12*'-=')
    print(f'O computador jogou {opcoes[computador]}')
    print(f'O jogador jogou {opcoes[jogador]}')
    print(12*'-=')
    if computador == 0:
        if jogador == 0:
            empate+=1
        elif jogador == 1:
            jogador_vence+=1
        elif jogador == 2:
            computador_vence+=1
    elif computador == 1:
        if jogador == 0:
            computador_vence+=1
        elif jogador == 1:
            empate+=1
        elif jogador == 2:
            jogador_vence+=1
    elif computador == 2:
        if jogador == 0:
            jogador_vence+=1
        elif jogador == 1:
            computador_vence+=1
        elif jogador == 2:
            empate+=1
    print(emojize(f'''\033[31mPONTUAÇÃO\033[m
Você:person_bald: : {jogador_vence}
Computador:laptop: : {computador_vence}'''))
    jogar=str(input('Deseja continuar a jogar?')).strip().upper()[0]
    while jogar not in 'S,N':
        jogar=str(input('Digite um dado válido [S/N]. Deseja continuar jogando?')).strip().upper()[0]
    print(12*'-=')
print('FIM DE JOGO!')
if jogador_vence > computador_vence:
    print(f'\n\033[32mVocê venceu o computador por {jogador_vence} a {computador_vence}.\033[m')
elif jogador_vence < computador_vence: 
    print(f'\n\033[31mO computador venceu você por {computador_vence} a {jogador_vence}.\033[m')
elif jogador_vence == computador_vence:
    print('\n\033[33mEmpatou!\033[m')