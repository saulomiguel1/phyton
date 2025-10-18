print('-'*31 + '\n ORDEM CRESCENTE E DECRESCENTE\n' + '-'*31)

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num2 < num1:
    aux = num2
    num2 = num1 
    num1 = aux

if num3 < num1:
    aux = num3
    num3 = num1
    num1 = aux

if num3 < num2:
    aux = num2
    num2 = num3
    num3 = aux

print(f'\nORDEM CRESCENTE: {num1} -> {num2} -> {num3}')
print(f'\nORDEM DECRESCENTE: {num3} -> {num2} -> {num1}')
 