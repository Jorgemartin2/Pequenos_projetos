from time import sleep
print(15*'\033[31m=-\033[m')
print('{:^35}'.format('\033[31mBANCO ALG\033[m'))
print(15*'\033[31m=-\033[m')
valor=int(input('Qual valor deseja sacar? R$'))
total=valor
cedula=50
total_cedula=0
while True:
    if total >= cedula:
        total-=cedula
        total_cedula+=1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cedulas de R${cedula}')
        if cedula == 50:
            cedula=20
        elif cedula == 20:
            cedula=10
        elif cedula == 10:
            cedula=1
        total_cedula=0
        if total == 0:
            break
print(15*'==')
print('Aguarde alguns segundos...')
sleep(3)
print('Saque realizado com \033[32mSUCESSO.\033[m')
print(15*'==')
print('Volte sempre ao \033[31mBANCO ALG!\033[m \nTe esperamos em breve.')