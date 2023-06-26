print(30*'=-')
print('                     BOLETIM ESCOLAR')
print(30*'=-')
ficha=[]
notas=[]
while True:
    nome=str(input('Nome: '))
    nota1=float(input(f'Nota 1º Bimestre: '))
    nota2=float(input('Nota 2º Bimestre: '))
    nota3=float(input('Nota 3º Bimestre: '))
    nota4=float(input('Nota 4º Bimestre: '))
    media=(nota1+nota2+nota3+nota4)/4
    ficha.append([nome, [nota1,nota2,nota3,nota4], media])
    print(25*'-')
    resposta=str(input('Quer continuar? ')).strip().upper()[0]
    print(25*'-')
    if resposta not in 'S,N':
        resposta=str(input('Digite um dado válido [S/N]. Quer continuar? ')).strip().upper()[0]
    if resposta in 'N':
        break
print(30*'=-')
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print(30*'=-')
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print(30*'--')
    opcao=int(input('Quer mostrar as notas de qual aluno? (999 finaliza o programa.)'))
    if opcao == 999:
        print()
        print('FINALIZANDO O PROGRAMA...')
        break
    if opcao <= len(ficha)-1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print()
print('<<< VOLTE SEMPRE >>>')