print('-'*25 + '\n   TESTE DE TRIÂNGULOS\n' + '-'*25)

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
  print('\nSão valores que podem formar um triângulo!')
  if num1 == num2 == num3:
    print('Esse triângulo é o EQUILÁTERO!\n')
  elif num1 == num2 or num1 == num3 or num2 == num3:
    print('Esse triângulo é o ISÓSCELES!\n')
  elif num1 != num2 != num3:
    print('Esse triângulo é o ESCALENO!\n')

else:
  print('\nValores não formam um triângulo!\n')