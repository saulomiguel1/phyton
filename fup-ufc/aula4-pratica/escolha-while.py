print('-' * 20 + '\n ESCOLHA 5 NÚMEROS\n' + '-' * 20)

i = 1
while i <= 5:
    num = int(input(f'{i}- Escolha um número: '))
    if num >= 100 and num <= 200:
        print(f'Número digitado: {num} // Você digitou um número entre 100 e 200! \n')
    else:
        print(f'Número digitado: {num} // Você digitou um número fora da faixa entre 100 e 200! \n')
    i += 1