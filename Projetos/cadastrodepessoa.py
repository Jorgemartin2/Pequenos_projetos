from time import sleep
dados={}
pessoas=[]
soma=media=0
print(f'''{"========================":^60}
{"<<< TELA DE CADASTRO >>>":^60}
{"========================":^60}''')
while True:
    dados['nome']=str(input('Nome: '))
    dados['sexo']=str(input('Sexo: ')).strip().upper()[0]
    if dados['sexo'] not in 'M,F':
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo']=str(input('Sexo: ')).strip().upper()[0]
    dados['idade']=int(input('Idade: '))
    soma+=dados['idade']
    pessoas.append(dados.copy())
    resposta=str(input('Quer continuar? ')).strip().upper()[0]
    if resposta not in 'S,N':
        print('ERRO! Responda apenas S ou N.')
        resposta=str(input('Quer continuar? ')).strip().upper()[0]
    if resposta in 'N':
        break
print('='*50)
sleep(1)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print('='*50)
media=soma/len(pessoas)
sleep(1)
print(f'B) A média da idade é de {media:5.2f} anos.')
print('='*50)
sleep(1)
print('C) As mulheres cadastradas foram a ', end='')
for pessoa in pessoas:
    if pessoa['sexo'] in 'F':
        print(f'{pessoa["nome"]}', end='')
print()
print('='*50)
sleep(1)
print('D) Lista das pessoas que estão acima da média: ')
for pessoa in pessoas:
    if pessoa['idade']>=media:
        print('')
        for keys, values in pessoa.items():
            print(f'{keys} = {values}; ', end='')
        print()
print()
print(f'{"<<< PROGRAMA ENCERRADO >>>":^60}')