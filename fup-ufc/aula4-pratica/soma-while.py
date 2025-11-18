print('-'*40 + '\n  SOMA DOS NÚMEROS INTEIROS DE 1 A 100\n' + '-'*40)

i = 1
soma = 0

while i <= 100:
    res = soma
    soma += i
    print (f'{res} + {i} = {soma}')
    i += 1
print(f'A soma dos números inteiros de 1 a 100 resulta em {soma}.')