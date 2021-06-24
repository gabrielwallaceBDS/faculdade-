#escreva umalgoritimo que leia um valor e que imprima a quantidade de cedulas necessarias para pagar esse memso valor para simplificar vamos trabalhar apenas com valores inteiros e com cedulas de r$100, r$50, r$20, r$10 r$5 e r$1

valor = int(input('qual valor a pagar?: '))

while True:
    if valor >= 100:
        cedulas100 = valor // 100
        valor = valor - cedulas100 * 100
        print('cedulas de 100 :{}'.format(cedulas100))
        if not valor:
            break
    if valor >= 50:
        cedulas50 = valor // 50
        valor = valor - cedulas50 * 50
        print('cedulas de 50 :{}'.format(cedulas50))
        if not valor:
            break
    if valor >= 20:
        cedulas20 = valor // 20
        valor = valor - cedulas20 * 20
        print('cedulas de 20 :{}'.format(cedulas20))
        if not valor:
            break
    if valor >= 100:
        cedulas10 = valor // 10
        valor = valor - cedulas10 * 10
        print('cedulas de 10 :{}'.format(cedulas10))
        if not valor:
            break
    if valor >= 5:
        cedulas5 = valor // 5
        valor = valor - cedulas5 * 5
        print('cedulas de 5 :{}'.format(cedulas5))
        if not valor:
            break
    if valor:
        cedulas1 = valor
        print('cedulas de 1: {}'.format(cedulas1))
        break