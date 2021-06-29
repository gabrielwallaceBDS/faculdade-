#escreva  um programa que pergunte a quantidade de km percorrido por um carro alugado pelo usuario, assim como a quantidade de dias pelos quais o carro foi alugado. calcule o preco a pagar, sabendo que o carro custa r$ 60 por dia e r$ 0,15 por km rodado

km = int(input('Quantos KM foram percorridos? '))
dias = int(input('Quantos dias ele foi alugado? '))

preco = 60 * dias + 0.15 * km
print('Km = {}. dias: {}'.format(km,dias))
print('valor a ser pago: {}'.format(preco))
