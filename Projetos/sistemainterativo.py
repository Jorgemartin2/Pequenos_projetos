from time import sleep
c=('\033[m',          #0-sem cor
   '\033[0;30;41m',   #1-vermelho
   '\033[0;30;42m',   #2-verde
   '\033[0;30;43m',   #3-amarelo
   '\033[0;30;44m',   #4-azul
   '\033[0;30;45m',   #5-roxo
   '\033[47m'       #6-branco
   );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 5)
    print(c[6])
    help(com)
    print(c[0])
    sleep(2)


def titulo(msg, cor=0):
    tamanho=len(msg)+4
    print(c[cor])
    print('='*tamanho)
    print(f'{  msg}')
    print('='*tamanho)
    print(c[0])
    sleep(1)


comando=''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando=str(input('Função ou biblioteca (Digite FIM caso queira encerrar o programa.) >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
