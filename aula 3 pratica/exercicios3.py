#ESCREVA UM PROGRAMA QUE CALCULE O PRECO A PAGAR PELO FORNECIMENTO DE ENERGIA ELETRICA. PERGUNTE A QUANTIDADE DE kWh CONSUMIDO E O TIPO DE INSTALACAO: R PARA RESIDENCIAS, I PARA INDUSTRIAS E C PARA COMERCIOS#
print('Preco a pagar de energia')
print('qual o tipo de instalacao que voce utiliza:\nR - residencias\nI - industrias\nC - comercios')
tipo = input('digite sua opcao:')
kwh = float(input('kWh utilizados: '))

if (tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif (tipo == 'I'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
elif (tipo == 'c'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.6
else: 
    print('Instalacao invalida')

print('total a pagar: {}'.format(kwh * preco))