print('{:=^40}'.format(' PAGAMENTO '))
valor_compra=float(input('Qual o valor total da compra? R$'))
print('''Escolha uma opção de pagamento:
[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] Em 3x ou mais no cartão''' )
opcao=int(input('Qual a opção que deseja fazer?'))
if opcao ==1:
        total=valor_compra-(valor_compra*10/100)
        print(f'Sua compra de R${valor_compra} saiu por R${total} com 10% de desconto.')
elif opcao ==2:
        total=valor_compra-(valor_compra*5/100)
        print(f'Sua compra de R${valor_compra} saiu por R${total} com 5% de desconto.')
elif opcao ==3:
        total=valor_compra
        parcela=valor_compra/2
        print(f'Sua compra será parcelada em 2x de R${parcela :.2f}')
elif opcao ==4:
        total=valor_compra+(valor_compra*20/100)
        parcela_desejada=int(input('Em quantas parcelas?'))
        parcelas=total/parcela_desejada
        print(f'Sua compra será parcelada em {parcela_desejada}x de R${parcelas} ')
else:
    print('\033[31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE!\033[m')
