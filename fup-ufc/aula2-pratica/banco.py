print('BANCO MEDEIROS\n' +'-'*40 + ' \nCÉDULAS: \nR$ 200.00 \nR$ 100.00 \nR$ 50.00 \nR$ 20.00 \nR$ 10.00 \nR$ 5.00 \nR$ 2.00')

valor = int(input('\nQual o valor do saque? R$ '))

if valor >= 200:    #Valor maior que 200 divide por ele e o resultado vai ser a quant de cédulas desse valor o resto (%) vai ser encaminhado para as prox opções
  quant = valor // 200
  print(f'\nVocê vai receber {quant} cédulas de 200')
  valor %= 200

if valor >= 100:    #Caso sobre valor ou seja menor que 200, divide por esse e o resultado vai ser a quant de cédulas desse valor o resto (%) vai ser encaminhado para as prox opções
  quant = valor // 100
  print(f'\nVocê vai receber {quant} cédulas de 100')
  valor %= 100

if valor >= 50: #Caso sobre valor ou seja menor que 100, divide por esse e o resultado vai ser a quant de cédulas desse valor o resto (%) vai ser encaminhado para as prox opções
  quant = valor // 50
  print(f'\nVocê vai receber {quant} cédulas de 50')
  valor %= 50

if valor >= 20: #Caso sobre valor ou seja menor que 50, divide por esse e o resultado vai ser a quant de cédulas desse valor o resto (%) vai ser encaminhado para as prox opções
  quant = valor // 20
  print(f'\nVocê vai receber {quant} cédulas de 20')
  valor %= 20

if valor >= 10: #Caso sobre valor ou seja menor que 20, divide por esse e o resultado vai ser a quant de cédulas desse valor o resto (%) vai ser encaminhado para as prox opções
  quant = valor // 10
  print(f'\nVocê vai receber {quant} cédulas de 10')
  valor %= 10

if valor >= 5:  #Caso sobre valor ou seja menor que 10, divide por esse e o resultado vai ser a quant de cédulas desse valor o resto (%) vai ser encaminhado para as prox opções
  quant = valor // 5
  print (f'\nVocê vai receber {quant} cédulas de 5')
  valor %= 5

if valor >= 2:  #Caso sobre valor ou seja menor que 5, divide por esse e o resultado vai ser a quant de cédulas desse valor o resto (%) vai ser encaminhado para as prox opções
  quant = valor // 2
  print (f'\nVocê vai receber {quant} cédulas de 2')
  valor %= 2

if valor % 2 == 1:  #Caso sobre valor ou seja menor que 2, não terá como fazer a operação!
  print(f'\nSobrou R$ {valor} pois não temos cédulas desse valor!')