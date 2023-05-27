soma_idade=0
maioridade_homem=0
nome_velho=''
total_mulheres=0
for n in range(1, 5):
    print(f'------ \033[35m{n}º PESSOA\033[m ------')
    nome=str(input('\033[31mNome: \033[m')).strip()
    idade=int(input('\033[32mIdade: \033[m'))
    sexo=str(input('\033[33mSexo [m/f]: \033[m')).strip().lower()
    soma_idade += idade
    if n == 1 and sexo in 'm':
        maioridade_homem=idade
        nome_velho=nome
    if sexo == 'm' and idade > maioridade_homem:
        maioridade_homem=idade
        nome_velho=nome
    if sexo == 'f' and idade < 20:
        total_mulheres += 1
media_idade=soma_idade/4
print(f'A média da idade do grupo é {media_idade}')
print(f'O homem mais velho se chama {nome_velho} e tem {maioridade_homem} anos de idade')
print(f'Ao todo temos {total_mulheres} mulheres com menos de 20 anos')