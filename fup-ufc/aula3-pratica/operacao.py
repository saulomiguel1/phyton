print('-'*25 + '\n        OPERAÇÕES\n' + '-'*25 + '\n1. Adição\n2. Subtração\n3. Divisão\n4. Multiplicação')
escolha = int(input('\nDigite a opção que você quer: '))

if escolha == 1:
  num1 = int(input('Digite o primeiro valor: '))
  num2 = int(input('Digite o segundo valor: '))
  soma = num1 + num2
  print(f'A soma de {num1} + {num2} é: {soma}')

elif escolha == 2:
  num1 = int(input('Digite o primeiro valor: '))
  num2 = int(input('Digite o segundo valor: '))
  sub = num1 - num2
  print(f'A subtração de {num1} - {num2} é: {sub}')

elif escolha == 3:
  num1 = float(input('Digite o primeiro valor: '))
  num2 = float(input('Digite o segundo valor: '))
  if num2 == 0:
    print('Divisão por zero não permitida')
  else:
    divi = num1 / num2
    print(f'A divisão de {num1} / {num2} é: {divi}')

elif escolha == 4:
  num1 = int(input('Digite o primeiro valor: '))
  num2 = int(input('Digite o segundo valor: '))
  mult = num1 * num2
  print(f'A multiplicação de {num1} x {num2} é: {mult}')

else:
  print('[ERRO] Valor inválido!')