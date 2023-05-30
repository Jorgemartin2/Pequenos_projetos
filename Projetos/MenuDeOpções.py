from time import sleep
print('==='*10)
print(' '*11,'MENU')
print('==='*10)
numero1=int(input('Primeiro valor: '))
numero2=int(input('Segundo valor: '))
opcao=0
while opcao != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR NÚMERO
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao=int(input('Qual a opção que deseja?'))
    if opcao == 1:
        resultado=numero1+numero2
        print(f'A soma entre {numero1} e {numero2} é igual a {resultado}')
    elif opcao == 2:
        resultado=numero1*numero2
        print(f'O resultado de {numero1} X {numero2} é igual a {resultado}')
    elif opcao == 3:
        if numero1 > numero2:
            maior=numero1
        elif numero2 > numero1:
            maior=numero2
            print(f'O maior numero entre {numero2} e {numero1} é {maior}')
        else:
            print('Os valores são iguais.')
    elif opcao == 4:
        print('Informe novamente os numeros: ')
        numero1=int(input('Primeiro valor: '))
        numero2=int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando o programa...')
        sleep(2)
    else:
        print('Opção Inválida. Tente novamente.')
    print('--'*15)
    sleep(2)
print('Fim do programa. Te espero em breve!')

