from random import randint
from time import sleep
print(43*'=')
print('                MEGA SENA')
print(43*'=')
quantidade=int(input('Quantos jogos você quer que eu sorteie? '))
print()
mega_sena=[]
jogos=[]
total=1
while total <= quantidade:
    contador=0
    while True:
        numero=randint(1,60)
        if numero not in mega_sena:
            mega_sena.append(numero)
            contador+=1
        if contador >= 6:
            break
    mega_sena.sort()
    jogos.append(mega_sena[:])
    mega_sena.clear()
    total+=1
print('-='*6, f'SORTEANDO {quantidade} JOGOS', '-='*6)
sleep(1)
for indice, lista in enumerate(jogos):
    print(f'JOGO {indice+1}: {lista}')
    print(43*'-')
    sleep(1)
print('-='*7, '< BOA SORTE >', '-='*7)
