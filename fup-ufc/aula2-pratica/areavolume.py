print('-'*29 + '\n Área e volume do CILINDRO \n' + '-'*29)
altura = float(input('Digite o valor da altura do cilindro: '))
raio = float(input('Digite o valor do raio do cilindro: '))

area = 2 * 3.14 * (raio) * (altura + raio)
vol = 3.14 * (raio) ** 2 * (altura)

print (f'O valor da área do cilindro é: {area} \nE o volume é: {vol}')