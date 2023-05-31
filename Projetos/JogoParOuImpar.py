from random import randint
from time import sleep
from emoji import emojize
vitoria=0
print('=-='*15)
print(emojize('\033[35mVAMOS JOGAR PAR:victory_hand: OU IMPAR:index_pointing_up:\033[m'))
print('=-='*15)
while True:
    jogador=int(input('Digite um valor: '))
    computador=randint(0, 10)
    total = jogador+computador
    tipo=' '
    while tipo not in 'P,I':
        tipo=str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    if total % 2 == 0:
        print('DEU PAR')
    else:
        print('DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[32mVOCÊ VENCEU!\033[m')
            vitoria+=1
        else:
            print('\033[31mVOCÊ PERDEU!\033[m')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('\033[32mVOCÊ VENCEU!\033[m')
            vitoria+=1
        else:
            print('\033[31mVOCÊ PERDEU!\033[m')
            break
    print('==='*15)
    print('Vamos jogar novamente...')
    print('==='*15)
    sleep(2)
print(emojize(f'\033[31m:police_car_light:GAME OVER:police_car_light:\033[mVocê ganhou {vitoria} vezes.'))