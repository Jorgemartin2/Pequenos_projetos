def notas(*n, sit=False, tab=False):
    dados={}
    total=maior=menor=soma=0
    s=''
    for i in n:
        soma+=i
        total+=1
        if i == n[0]:
            maior=i
            menor=i
        else:
            if i > maior:
                maior=i
            if i < menor:
                menor=i
    media=soma/total
    if media < 5:
        s='RUIM'
    if 5 <= media < 7:
        s='RAZOÁVEL'
    if media > 7: 
        s='BOA'
    dados['total']=total
    dados['menor']=menor
    dados['maior']=maior
    dados['media']=media
    if sit == True:
        dados['situacao']=s
    if tab == True:
        if sit == True:
            print()
            print('='*50)
            print(f'\033[1;34;43m{"ALUNOS DA SALA (NOTAS)":^50}\033[m')
            print('='*50)
            print(f'{"Total":<10}{"Maior":<10}{"Menor":<10}{"Média":<10}{"Situação":<12}')
            print('-'*50)
            print(f'{dados["total"]:<10}{dados["maior"]:<10}{dados["menor"]:<10}{dados["media"]:<10.3f}{dados["situacao"]:<12}')
            print()
        else:
            print()
            print('='*37)
            print(f'\033[1;34;43m{"ALUNOS DA SALA (NOTAS)":^37}\033[m')
            print('='*37)
            print(f'{"Total":<10}{"Maior":<10}{"Menor":<10}{"Média":<10}')
            print('-'*37)
            print(f'{dados["total"]:<10}{dados["maior"]:<10}{dados["menor"]:<10}{dados["media"]:<10.3f}')
            print()
    return dados


num=[]
while True:
    g=float(input('Digite a nota: '))
    num.append(g)
    r=str(input('Deseja continuar? ')).strip().upper()[0]
    if r == 'N':
        break
print('-'*40)
situation=str(input('Deseja mostrar a situação? ')).strip().upper()[0]
tabela=str(input('Deseja mostrar em tabela? ')).strip().upper()[0]
if situation == 'S':
    if tabela == 'S':
        resp=notas(*num, sit=True, tab=True)
    else:
        resp=notas(*num, sit=True)
else:
    if tabela == 'S':
        resp=notas(*num, tab=True)
    else:
        resp=notas(*num)
print()
print(resp)
