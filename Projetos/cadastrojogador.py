print(f'{"<<<--- CADASTRO --->>>":^40}')
jogador={}
time=[]
gols=[]
while True:
    jogador['nome']=str(input('Nome do jogador: '))
    partidas=int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
    gols.clear()
    for contador in range(0, partidas):
        gols.append(int(input(f'  Quantos gols na {contador+1}ª partida? ')))
    jogador['gols']=gols[:]
    jogador['total']=sum(gols)
    time.append(jogador.copy())                  
    resposta=str(input('Quer continuar? ')).strip().upper()[0]
    if resposta not in 'S,N':
        print('ERRO! Por favor, digite SIM ou NÃO.')
        resposta=str(input('Quer continuar? ')).strip().upper()[0]
    if resposta in 'N':
        break
print('=-'*30)
print('Cód', end='')
for elemento in jogador.keys():
    print(f'{elemento:>15}', end='')
print()
print('--'*30)
for keys, values in enumerate(time):
    print(f'{keys:>3}', end='')
    for dado in values.values():
        print(f'{str(dado):>15}', end='')
    print()
print('--'*30)
while True:
    busca=int(input('Quer mostrar os dados de qual jogador? (999 ENCERRA)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}!')
    else:
        print(f'=> LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for indice, gol in enumerate(time[busca]["gols"]):
            print(f'No jogo {indice+1} fez {gol} gols.')
    print('--'*30)
print('PROGRAMA ENCERRADO!')
print('<<< VOLTE SEMPRE >>>')
