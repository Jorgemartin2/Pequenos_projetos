from time import sleep


def mensagem(msg):
    tamanho=len(msg)+10
    print('='*tamanho)
    print(f'     {msg}')
    print('='*tamanho)
mensagem('CONTADOR')


def contador(inicio, fim, passo):
    print('-'*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)
    if inicio < fim:
        contador=inicio
        while contador <= fim:
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador+=passo
        print('FIM!')
        print('-'*30)
    else:
        contador=inicio
        while contador >= fim:
            print(f'{contador} ', end='', flush=True)
            sleep(0.5)
            contador-=passo
        print('FIM!')
        print('-'*30)


contador(1,10,1) 
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem!')
print('-'*30)
while True:
    inicio=int(input('Inicio: '))
    fim=int(input('Fim: '))
    passo=int(input('Passo: '))
    contador(inicio, fim, passo)
    resposta=str(input('Quer continuar? ')).strip().upper()[0]
    print('-'*30)
    if resposta not in 'S,N':
        print('ERRO! Digite apenas SIM ou NÃO.')
        resposta=str(input('Quer continuar? ')).strip().upper()[0]
    if resposta in 'N':
        break
mensagem('PROGRAMA ENCERRADO!')
print(mensagem)